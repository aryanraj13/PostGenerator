import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)