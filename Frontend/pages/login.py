import streamlit as st
import requests
from streamlit_local_storage import LocalStorage

localStoreage = LocalStorage()

st.title("Login")

Backend_URL = "https://full-stack-ai-learning-assistant.onrender.com"

with st.form("Login"):
    email = st.text_input("Email")
    password = st.text_input("Password",type="password")
    role = st.selectbox("Role",["Student","Faculty"])
    login_button =st.form_submit_button("Login")

    if login_button:
        payload = {
            "email":email,
            "password":password,
            "role":role
        }
        res = requests.post(f"{Backend_URL}/login",json=payload)
        # st.write(res)
        # st.write(res.json()["msg"]) 
        # st.write(res.json()["msg"][0])
        data = res.json()["msg"]

        if isinstance(data,list):
            localStoreage.setItem("logged_User",data[0])
            loggedIn_User = localStoreage.getItem("logged_User")
            LoggedIn_mail = loggedIn_User["email"]
            LoggedIn_role = loggedIn_User["role"]

            if LoggedIn_role == "Faculty":
                st.switch_page("pages/FacultyDashboard.py")
            else :
                st.switch_page("pages/StudentDashboard.py")


