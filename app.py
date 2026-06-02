import streamlit as st
from google import genai
import time

st.set_page_config(page_title="MoodGPT", page_icon="🎭", layout="centered")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

MOODS = {
    "Funny": "You are a hilarious comedian. Keep responses witty and entertaining.",
    "Angry": "You are dramatically angry but still funny and safe.",
    "Defensive": "You are slightly defensive and always justify yourself humorously.",
    "Friendly": "You are warm, kind, and supportive.",
    "Chaotic": "You are unpredictable, random, and absurd."
}

if "chat" not in st.session_state:
    st.session_state.chat = []

def ask_gemini(message, mood):
    prompt = f"""
{MOODS[mood]}

Conversation:
{st.session_state.chat}

User: {message}
Assistant:
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


st.title("🎭 MoodGPT")

mood = st.selectbox("Mood", list(MOODS.keys()))

chat_container = st.container()

with chat_container:
    for role, msg in st.session_state.chat:
        if role == "user":
            st.markdown(
                f"""
                <div style="display:flex;justify-content:flex-end;margin:10px 0;">
                    <div style="background:#2b6cff;color:white;padding:10px 14px;border-radius:15px;max-width:70%;">
                        🧑 {msg}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="display:flex;justify-content:flex-start;margin:10px 0;">
                    <div style="background:#2a2a2a;color:white;padding:10px 14px;border-radius:15px;max-width:70%;">
                        🤖 {msg}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

user_input = st.text_input("Message", label_visibility="collapsed", placeholder="Type something...")

col1, col2 = st.columns([1, 5])
send = col1.button("Send")

if send and user_input:
    st.session_state.chat.append(("user", user_input))

    typing_placeholder = st.empty()
    typing_placeholder.markdown("🤖 MoodGPT is typing...")

    time.sleep(0.6)

    reply = ask_gemini(user_input, mood)

    typing_placeholder.empty()

    st.session_state.chat.append(("bot", reply))

    st.rerun()
