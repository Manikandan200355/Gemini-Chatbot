import streamlit as st 
import google.generativeai as genai

st.title("Welcome to Gemini Chat")

genai.configure(api_key="")

text = st.text_input("Enter Your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Generate"):
    response = chat.send_message(text)

    st.write(response.text) 
