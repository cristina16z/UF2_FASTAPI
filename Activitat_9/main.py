import connection
import user_sch
import users
from fastapi import FastAPI
from typing import List

app = FastAPI()



@app.get ("/users", response_model=List[dict])
async def read_users():
    db_connection = connection.connection_db()
    return user_sch.users_schema(users.read(db_connection))