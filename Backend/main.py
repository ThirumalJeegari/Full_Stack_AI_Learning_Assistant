from fastapi import FastAPI, UploadFile, File, Form
from database import supa_base

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Backend Running Successfully"}


@app.post("/signup")
def signup(payload: dict):

    supa_base.table("users").insert(payload).execute()

    return {
        "msg": "User Registered Successfully"
    }


@app.post("/login")
def login(payload: dict):

    res = (
        supa_base.table("users")
        .select("*")
        .eq("email", payload["email"])
        .eq("password", payload["password"])
        .eq("role", payload["role"])
        .execute()
    )

    return {
        "msg": res.data
    }

@app.post("/upload")
async def upload_file(
    student_id: str = Form(...),
    file: UploadFile = File(...)
):

    file_bytes = await file.read()

    file_path = f"{student_id}/{file.filename}"

    print("Uploading:", file_path)

    supa_base.storage.from_("assignments").upload(
        file_path,
        file_bytes
    )

    file_url = supa_base.storage.from_("assignments").get_public_url(file_path)

    print("URL:", file_url)

    supa_base.table("assignments").insert({
        "student_id": student_id,
        "assigment_url": file_url
    }).execute()

    return {
        "success": True,
        "file_url": file_url
    }

@app.get("/assignments")
def get_assignments():

    res = (supa_base.table("assignments").select("*").execute())

    return {
        "data": res.data
    }