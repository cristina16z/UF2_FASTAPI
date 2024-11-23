import db_connect.connection as connection
import schemas.user_sch as user_sch
import crud.readUsers as readUsers
from fastapi import FastAPI
from typing import List

app = FastAPI()



@app.get ("/users", response_model=List[dict])
async def read_users():
    db_connection = connection.connection_db()
    return user_sch.users_schema(readUsers.read(db_connection))