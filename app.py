import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")
st.title("🤖 Gemini AI Assistant")

# --- API KEY CONFIGURATION ---
# Option 1: Streamlit Cloud Secrets (Recommended)
# Option 2: Direct Key (If Secrets not used)
DIRECT_API_KEY = "AIzaSy_YOUR_ACTUAL_API_KEY_HERE"

# Try getting key from Streamlit Secrets first, fallback to DIRECT_API_KEY
API_KEY = st.secrets.get("GEMINI_API_KEY", DIRECT_API_KEY)

# Validation check
if not API_KEY or API_KEY == "AIzaSy_YOUR_ACTUAL_API_KEY_HERE":
    st.warning("⚠️ Please provide a valid Gemini API Key in Streamlit Secrets or update DIRECT_API_KEY in app.py!")
    st.stop()

# Configure Google Gemini
genai.configure(api_key=API_KEY.strip())

# Initialize Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input & Assistant Response
if prompt := st.chat_input("Ask me anything..."):
    # Append user prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from Gemini
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error generating response: {e}")
