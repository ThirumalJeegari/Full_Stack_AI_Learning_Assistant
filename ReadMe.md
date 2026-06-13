AI Agent Learning Assistant

An AI-powered Learning Assistant built using Streamlit, FastAPI, and Supabase. This application provides authentication for Students and Faculty members with separate dashboards.

🚀 Features

User Signup
User Login Authentication
Role-Based Access (Student / Faculty)
Browser Local Storage Session Management
Separate Dashboards for Students and Faculty
Backend API using FastAPI
Database integration using Supabase

🛠️ Tech Stack
Frontend
Streamlit
Requests
streamlit-local-storage
Backend
FastAPI
Supabase Python SDK
Database
Supabase PostgreSQL Database

📂 Project Structure
AI-Agent-Learning-Assistant/
│
├── app.py                    # Home Page
├── database.py               # Supabase Connection
├── main.py                   # FastAPI Backend APIs
│
├── pages/
│   ├── signup.py             # Signup Page
│   ├── login.py              # Login Page
│   ├── StudentDashboard.py   # Student Dashboard
│   └── FacultyDashboard.py   # Faculty Dashboard
│
└── README.md

⚙️ Installation

1. Clone the Repository
git clone https://github.com/yourusername/AI-Agent-Learning-Assistant.git

cd AI-Agent-Learning-Assistant

2. Create Virtual Environment
python -m venv venv

Activate Environment:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install streamlit fastapi uvicorn requests supabase streamlit-local-storage
🔧 Configure Supabase

Open database.py and update your credentials:

SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"

🗄️ Create Database Table

Create a table named users in Supabase with the following columns:

Column Name	Data Type
id	int
name	text
email	text
password	text
role	text

▶️ Run Backend Server

Start FastAPI server:

uvicorn main:app --reload

Backend will run on:

http://127.0.0.1:8000

▶️ Run Frontend Application

Start Streamlit application:

streamlit run app.py

Application will run on:

http://localhost:8501

🔐 API Endpoints

Signup API
POST /signup

Request Body:

{
    "name": "John",
    "email": "john@example.com",
    "password": "1234",
    "role": "Student"
}

Response:

{
    "msg": "user data inserted successfully..."
}
Login API
POST /login

Request Body:

{
    "email": "john@example.com",
    "password": "1234",
    "role": "Student"
}

Response:

{
    "msg": [
        {
            "name": "John",
            "email": "john@example.com",
            "role": "Student"
        }
    ]
}

👨‍🎓 User Roles

Student
Access Student 

Faculty
Access Faculty Dashboard

🔮 Future Enhancements

Password Hashing using bcrypt
JWT Authentication
Logout Functionality
AI Chatbot Integration
Course Management System
Assignment Uploads
Attendance Tracking
Learning Analytics Dashboard

📸 Screens

Home Page
Signup Page
Login Page
Student Dashboard
Faculty Dashboard


👨‍💻 Author
Thirumal Jeegari

