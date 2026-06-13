from fastapi import FastAPI
from database import supa_base


app = FastAPI()

@app.post("/signup")
def signup(payload:dict):
    res = supa_base.table("users").insert(payload).execute()

    return{
        "msg":"user data inserted successfully..."
    }

@app.post("/login")
def login(payload:dict):
    res = supa_base.table("users").select("*").eq("email",payload["email"]).eq("password",payload["password"]).eq("role",payload["role"]).execute()

    if len(res.data) == 0:
        return{
            "msg":"No Data Found!"
        }
    else:
        return{
            "msg":res.data
        }

