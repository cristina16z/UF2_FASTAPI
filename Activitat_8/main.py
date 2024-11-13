from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    password: str
    email: str
    sex: str
    age: int | None = None



@app.get("/")
async def root():
    return {"message": "Mètode GET"}


@app.post("/create-user/")
async def create_user(user: User):
    return user