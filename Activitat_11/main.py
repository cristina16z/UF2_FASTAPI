from fastapi import FastAPI
from typing import List
import insertData.connection as connection
import schemas.schemas as schemas
import crud.read as read



app = FastAPI()
db_connection = connection.connection_db()


