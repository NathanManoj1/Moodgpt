# 🎭 MoodGPT

A mood-based AI chatbot that changes personality based on how you're feeling, powered by Google's Gemini API.

---

## 📸 Demo
<img width="964" height="615" alt="image" src="https://github.com/user-attachments/assets/929b5983-9db2-4ebc-b269-abd190056cab" />


---

## 🚀 Try it live

👉 **[Open MoodGPT](https://moodgpt.streamlit.app/)**

---

## ⚡ Quick start

Just open the app and start chatting.

If running locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Make sure you add your API key in Streamlit secrets:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

---

## ✨ Features

* 🎭 5 personality moods (Funny, Angry, Defensive, Friendly, Chaotic)
* 💬 ChatGPT-style conversation UI with bubbles
* 🤖 AI responses powered by Gemini
* 🧠 Conversation memory within session
* ⏳ Typing indicator for more natural feel
* 🌙 Clean dark-themed interface

---

## 🧠 How it works

MoodGPT sends your message + selected personality style to the Gemini API. The AI then responds in that “mood,” making the same question feel completely different depending on the selected tone.

The UI is built using Streamlit and custom HTML/CSS to mimic a ChatGPT-style chat layout, with left/right message alignment and simple animations for a more dynamic feel.

---

## ⚙️ Tech stack

* Python
* Streamlit
* Google Gemini API
* HTML/CSS (custom chat bubbles)

---

## 📦 Setup notes

* Requires Python 3.10+
* Needs a Gemini API key from Google AI Studio
* Uses Streamlit Cloud for deployment

---

## 🙌 Credits

Built by Nathan for the Hack Club Stardance Challenge.

Powered by:

* Google Gemini API
* Streamlit
