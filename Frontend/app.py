import streamlit as st

st.title("AI_Learning_Assistant")

if st.button("Signup"):
    st.switch_page("pages/signup.py")

if st.button("Login"):
    st.switch_page("pages/login.py")
