import streamlit as st
import requests

st.title("Signup")

Backend_URL = "http://127.0.0.1:8000"

with st.form("Signup"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password",type ="password")
    role = st.selectbox("Role",["Student","Faculty"])
    signup_button = st.form_submit_button("Signup")
    login_button = st.form_submit_button("Login")

    if login_button:
        st.switch_page("pages/login.py")


    if signup_button:
        payload ={
            "name":name,
            "email":email,
            "password":password,
            "role":role
        }
        res = requests.post(f"{Backend_URL}/signup",json=payload)
        st.write(res)

