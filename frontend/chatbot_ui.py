import streamlit as st
import requests

st.title("IT Consulting Chatbot 🤖")

question = st.text_input("Ask me anything about our services:")

if st.button("Get Answer"):
    if question:
        response = requests.get("http://127.0.0.1:8000/faq", params={"question": question})
        st.write(response.json()["answer"])

st.subheader("Interested in a consultation?")
name = st.text_input("Your Name")
email = st.text_input("Your Email")

if st.button("Submit Info"):
    response = requests.post("http://127.0.0.1:8000/collect_info/", data={"name": name, "email": email})
    st.success(response.json()["message"])
