from langchain_groq import ChatGroq
import streamlit as st

st.write("Secrets available:", dict(st.secrets))

llm = ChatGroq(
    api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile",
)