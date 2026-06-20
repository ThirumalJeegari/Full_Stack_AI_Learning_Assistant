import streamlit as st
import requests
from streamlit_local_storage import LocalStorage

ls = LocalStorage()

Backend_URL = "http://127.0.0.1:8000"

st.title("Login")

with st.form("login_form"):

    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    role = st.selectbox("Role",["Student", "Faculty"])

    login_btn = st.form_submit_button("Login")

    if login_btn:

        payload = {
            "email": email,
            "password": password,
            "role": role
        }

        res = requests.post(f"{Backend_URL}/login",json=payload)

        data = res.json()["msg"]

        if len(data) > 0:

            ls.setItem("logged_User",data[0])

            if role == "Student":
                st.switch_page("pages/StudentDashboard.py")
            else:
                st.switch_page("pages/FacultyDashboard.py")
        else:
            st.error("Invalid Credentials")