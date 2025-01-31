import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate"

st.set_page_config(page_title="OpenAI Alternative Chat", layout="wide")
st.title("OpenAI Alternative - Better Than DeepSeek")

st.sidebar.header("Settings")
max_length = st.sidebar.slider("Max Length", min_value=10, max_value=512, value=256)
temperature = st.sidebar.slider("Temperature", min_value=0.1, max_value=1.0, value=0.7)

st.subheader("Chat with AI")
prompt = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    response = requests.post(
        API_URL,
        json={"prompt": prompt, "max_length": max_length, "temperature": temperature},
    )
    if response.status_code == 200:
        st.success("### AI Response:")
        st.write(response.json()["response"])
    else:
        st.error("Failed to generate response.")
