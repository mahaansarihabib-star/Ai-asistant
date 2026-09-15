import streamlit as st
from google import genai

# Page setup
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")
st.title("🤖 Gemini AI Assistant")

# Initialize Gemini Client using Streamlit Secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize session state for message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask me anything..."):
    # Append and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response using Gemini
    with st.chat_message("assistant"):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        st.markdown(response.text)

    # Store assistant response in session state
    st.session_state.messages.append({"role": "assistant", "content": response.text})