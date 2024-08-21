import streamlit as st 
import google.generativeai as genai

st.title("Welcome to Gemini Chat")

genai.configure(api_key="AIzaSyAxY2JX6XvbHQLW6s1AIyHf3jFbf8FEJ34")

text = st.text_input("Enter Your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message(text)
st.write(response.text)

if st.text_button("Generate"):
    response = chat.send_message(text)
    st.write(response.text) 