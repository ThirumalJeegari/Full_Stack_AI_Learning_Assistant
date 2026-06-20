import streamlit as st
import requests
from streamlit_local_storage import LocalStorage

ls = LocalStorage()

server_url = "http://127.0.0.1:8000"

st.title("Student Dashboard")

user = ls.getItem("logged_User")

if user is None:
    st.error("Please Login")
    st.stop()

st.write("Welcome:", user["name"])

pdf_file = st.file_uploader("Upload Assignment",type=["pdf"])

if st.button("Submit Assignment"):
    if pdf_file is not None:
        files = {
            "file": (
                pdf_file.name,
                pdf_file.getvalue()
            )
        }

        data = {"student_id": str(user["id"])}

        res = requests.post(f"{server_url}/upload",files=files,data=data)
        result = res.json()
        
        st.success("Assignment Uploaded Successfully")
        st.write(result["file_url"])