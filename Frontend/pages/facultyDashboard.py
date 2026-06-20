import streamlit as st
import requests

server_url = "http://127.0.0.1:8000"

st.title("Faculty Dashboard")

res = requests.get(f"{server_url}/assignments")

data = res.json()["data"]

if len(data) == 0:

    st.warning("No Assignments Submitted Yet")

else:
    for row in data:
        st.subheader(f"Student ID : {row['student_id']}")

        st.link_button("View Assignment",row["assigment_url"])
        st.divider()