import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# --------- SETUP ---------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Missing GEMINI_API_KEY in .env file")
    st.stop()

client = genai.Client(api_key=api_key)

# --------- SESSION STATE ---------
if "chats" not in st.session_state:
    st.session_state.chats = {"Chat 1": []}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"

if "hint_level" not in st.session_state:
    st.session_state.hint_level = 0

if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = 0

if "answers_taken" not in st.session_state:
    st.session_state.answers_taken = 0


# --------- AI FUNCTION WITH MEMORY ---------
def get_ai_response(chat_history, hint_level):

    # Hint behavior
    if hint_level == 0:
        instruction = "Guide step-by-step. Do NOT give final answer."
    elif hint_level == 1:
        instruction = "Give a small hint only."
    elif hint_level == 2:
        instruction = "Give a strong hint."
    else:
        instruction = "Give full answer with explanation."

    # 🔥 Trim history to avoid token overflow
    trimmed_history = chat_history[-10:]

    # 🔥 Build conversation string
    conversation = ""
    for msg in trimmed_history:
        role = "Student" if msg["role"] == "user" else "Teacher"
        conversation += f"{role}: {msg['content']}\n"

    prompt = f"""
    You are a strict but helpful teacher.

    Conversation so far:
    {conversation}

    Current Hint Level: {hint_level}
    Instruction: {instruction}

    RULES:
    1. Follow hint level strictly
    2. Continue the conversation (DO NOT restart)
    3. Refer to student's previous answers
    4. Keep responses short
    5. Ask guiding questions

    Now respond as the teacher:
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )

    return response.text.strip()


# --------- SIDEBAR ---------
st.sidebar.title("💬 Chats")

# Switch chats
for chat in st.session_state.chats.keys():
    if st.sidebar.button(chat):
        st.session_state.current_chat = chat
        st.session_state.hint_level = 0

# New chat
if st.sidebar.button("➕ New Chat"):
    new_chat = f"Chat {len(st.session_state.chats) + 1}"
    st.session_state.chats[new_chat] = []
    st.session_state.current_chat = new_chat
    st.session_state.hint_level = 0


# --------- MAIN UI ---------
st.title("🧠 AI Study Buddy")

chat_history = st.session_state.chats[st.session_state.current_chat]

# Display messages
for msg in chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# --------- USER INPUT ---------
user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.hint_level = 0
    st.session_state.questions_asked += 1

    # Add user message
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Get AI response WITH MEMORY
    response = get_ai_response(chat_history, 0)

    # Add AI response
    chat_history.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()


# --------- HINT BUTTON ---------
if st.button("💡 Hint"):
    if chat_history:

        # Find last user message
        last_user_msg = None
        for msg in reversed(chat_history):
            if msg["role"] == "user":
                last_user_msg = msg["content"]
                break

        if last_user_msg:
            st.session_state.hint_level += 1

            if st.session_state.hint_level == 3:
                st.session_state.answers_taken += 1

            level = min(st.session_state.hint_level, 3)

            # 🔥 Pass FULL chat history (NOT string)
            response = get_ai_response(chat_history, level)

            chat_history.append({
                "role": "assistant",
                "content": response
            })

            st.rerun()


# --------- STATS ---------
st.divider()
st.subheader("📊 Stats")

q = st.session_state.questions_asked
a = st.session_state.answers_taken

dependency = (a / q) * 100 if q > 0 else 0

st.write(f"Total Questions: {q}")
st.write(f"Answers Taken: {a}")
st.write(f"Dependency: {round(dependency, 2)}%")