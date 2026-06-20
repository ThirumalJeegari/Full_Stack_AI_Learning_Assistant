import streamlit as st
import requests

Backend_URL = "http://127.0.0.1:8000"

st.title("Signup")

with st.form("signup_form"):

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role",["Student", "Faculty"])
    signup_btn = st.form_submit_button("Signup")

    if signup_btn:
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }

        requests.post(f"{Backend_URL}/signup",json=payload)
        st.success("Signup Successful")

if st.button("Go To Login"):
    st.switch_page("pages/login.py")