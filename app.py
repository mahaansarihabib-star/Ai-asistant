import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")
st.title("🤖 Gemini AI Assistant")

# DIRECT KEY INSERTION (Testing ke liye)
# Yahan "YOUR_GEMINI_API_KEY" ki jagah apni actual key paste karein:
API_KEY = "AQ.Ab8RN6JrI39GXX6BWRREMY5s-CS0z3QHQFKiKyn-anWbvZkXXQ"

if API_KEY == "YOUR_GEMINI_API_KEY":
    st.warning("Pehle code mein line 9 par apni actual Gemini API key paste karein!")
    st.stop()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)

    st.session_state.messages.append({"role": "assistant", "content": response.text})
