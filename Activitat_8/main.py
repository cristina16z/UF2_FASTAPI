from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    password: str
    email: str
    sex: str
    age: int | None = None


# Mètode GET
@app.get("/")
async def root():
    return {"message": "Mètode GET"}


# Mètode POST creació d'usuari amb BaseModel
@app.post("/create-user/")
async def create_user(user: User):
    return user


# Mètode GET Error 400 HTTPException
@app.get("/get-no-funcional/")
async def red_user():
    raise HTTPException(
        status_code=400,
        detail="Registre no detectat"
    )
