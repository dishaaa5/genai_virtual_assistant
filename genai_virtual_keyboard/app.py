# app.py

from langchain_community.llms import Ollama
import streamlit as st
import speech_recognition as sr

# Set page title
st.set_page_config(page_title="🎙️ GenAI Virtual Assistant")
st.title("🎙️🧠 GenAI Virtual Keyboard & Voice Assistant")

# Load LLM (lightweight model for low RAM systems)
llm = Ollama(model="tinyllama")  # Also try "phi3" or "llama2:3b-chat" if needed

# Voice input section
st.subheader("🎤 Voice Input")
if st.button("🎙️ Start Listening"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            st.success(f"🗣️ You said: {query}")
        except sr.UnknownValueError:
            st.error("😕 Sorry, I couldn't understand your voice.")
            query = None
        except sr.RequestError:
            st.error("❌ Could not request results from Google Speech API.")
            query = None

        if query:
            with st.spinner("🤖 Generating response..."):
                response = llm.invoke(query)
                st.markdown("### 💬 Response:")
                st.write(response)

# Text input section
st.subheader("⌨️ Keyboard Input")
user_input = st.text_input("Type your question below:")

if user_input:
    with st.spinner("🤖 Generating response..."):
        response = llm.invoke(user_input)
        st.markdown("### 💬 Response:")
        st.write(response)
