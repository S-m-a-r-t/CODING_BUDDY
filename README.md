🧠 AI Study Buddy

An interactive AI-powered learning assistant that helps students think, not just get answers.
Built with Streamlit + Gemini API, this tool simulates a strict but helpful teacher using a guided hint system.

🚀 Features
💬 ChatGPT-like Interface – Smooth conversational UI
🧠 Context-Aware Memory – Remembers past messages in a session
🧩 Multi-Level Hint System
Level 0 → Guiding question
Level 1 → Small hint
Level 2 → Strong hint
Level 3 → Full solution
📊 Learning Analytics Dashboard
Tracks questions asked
Tracks answers taken
Calculates dependency %
🔄 Multiple Chat Sessions – Start and manage different conversations
⚙️ Tech Stack
Frontend: Streamlit
Backend: Python
AI Model: Google Gemini API
Environment Management: dotenv
State Management: Streamlit Session State
🏗️ How It Works
User asks a question
Chat history is stored in session
Context is passed to the AI model
AI responds based on hint level
User can request hints progressively

👉 The system ensures learning through guidance instead of direct answers

🧠 Memory System

Stores conversation as structured messages:

{"role": "user", "content": "question"}
Passes last few messages to AI for context
Enables continuous conversation flow
📊 Analytics

The system tracks:

Total questions asked
Number of full answers taken
Dependency percentage

This helps users understand their learning behavior

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/ai-study-buddy.git
cd ai-study-buddy
2. Install dependencies
pip install -r requirements.txt
3. Setup environment variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here
▶️ Run the App
streamlit run app.py
⚠️ Limitations
Session-based memory (resets on refresh)
Token limit for long conversations
No persistent database (yet)
🚀 Future Improvements
🔐 User Authentication (Firebase)
💾 Database Integration (MongoDB)
🧠 Long-term Memory (Vector DB)
🎤 Voice-based Interaction
🎯 Personalized Learning Paths
🤝 Contributing

Feel free to fork this repo and improve it!
Pull requests are welcome.

📄 License

This project is for educational purposes.

👨‍💻 Author

Akshat Saini
BTech CSE, Bennett University

GitHub: https://github.com/S-m-a-r-t
LinkedIn: https://www.linkedin.com/in/akshat-saini-626142255/
🔥 Final Note

This project focuses on a key idea:

“The goal of AI in education is not to give answers, but to build thinking.”
