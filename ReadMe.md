# 🎓 Full_Stack_AI_Learning_Assistant

An AI-powered Learning Management System built using **Streamlit**, **FastAPI**, and **Supabase**. The platform provides role-based authentication and separate dashboards for Students and Faculty.

---

## 🚀 Features

✅ User Signup & Login  
✅ Role-Based Access (Student / Faculty)  
✅ Browser Local Storage Session Management  
✅ Student Dashboard  
✅ Faculty Dashboard  
✅ FastAPI Backend APIs  
✅ Supabase Database Integration  
✅ Responsive Streamlit Interface  

---

## 🛠️ Tech Stack

### Frontend
- Streamlit
- Requests
- streamlit-local-storage

### Backend
- FastAPI
- Uvicorn
- Supabase Python SDK

### Database
- Supabase (PostgreSQL)

---

## 📁 Project Structure

```bash
LearnMate-AI/
│
├── Backend/
│   ├── main.py
│   └── database.py
│
├── Frontend/
│   ├── app.py
│   │
│   └── pages/
│       ├── signup.py
│       ├── login.py
│       ├── StudentDashboard.py
│       └── FacultyDashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/LearnMate-AI.git

cd LearnMate-AI
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file:

```bash
pip install streamlit fastapi uvicorn requests supabase streamlit-local-storage
```

---

## 🔧 Configure Supabase

Update your Supabase credentials in `database.py`:

```python
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"
```

---

## 🗄️ Database Schema

Create a table named **users** with the following columns:

| Column | Type |
|--------|------|
| id | int |
| name | text |
| email | text |
| password | text |
| role | text |

---

## ▶️ Run Backend Server

Navigate to the Backend folder:

```bash
cd Backend
uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

---

## ▶️ Run Frontend

Navigate to the Frontend folder:

```bash
cd Frontend
streamlit run app.py
```

Application runs on:

```bash
http://localhost:8501
```

---

## 🔐 API Endpoints

### Signup

```http
POST /signup
```

Request:

```json
{
    "name": "John",
    "email": "john@gmail.com",
    "password": "1234",
    "role": "Student"
}
```

Response:

```json
{
    "msg": "user data inserted successfully..."
}
```

---

### Login

```http
POST /login
```

Request:

```json
{
    "email": "john@gmail.com",
    "password": "1234",
    "role": "Student"
}
```

Response:

```json
{
    "msg": [
        {
            "name": "John",
            "email": "john@gmail.com",
            "role": "Student"
        }
    ]
}
```

---

## 🎯 User Roles

### 👨‍🎓 Student
- Access Student Dashboard

### 👨‍🏫 Faculty
- Access Faculty Dashboard

---

## 🔮 Future Enhancements

- 🔐 JWT Authentication
- 🔒 Password Hashing (bcrypt)
- 🚪 Logout Functionality
- 🤖 AI Chatbot Integration
- 📚 Course Management
- 📝 Assignment Upload
- 📊 Learning Analytics
- 🎯 Personalized Recommendations

---

## 📸 Screenshots

- Home Page
- Signup Page
- Login Page
- Student Dashboard
- Faculty Dashboard

> Add screenshots in a `/screenshots` folder and embed them here.

---

## 👨‍💻 Author

**Thirumal Jeegari**

- GitHub: `https://github.com/ThirumalJeegari`
- LinkedIn: `https://linkedin.com/in/thirumaljeegari`



