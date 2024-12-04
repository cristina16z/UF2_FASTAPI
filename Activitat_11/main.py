from fastapi import FastAPI
from typing import List
import insertData.connection as connection
import schemas.schemas as schemas
import crud.read as read



app = FastAPI()
db_connection = connection.connection_db()


@app.get ("/start-game", response_model=List[dict])
async def start_game():
    read_txt = read.read_start_game(db_connection)
    return schemas.startGames_schema(read_txt)

##
@app.get ("/num-errors", response_model=List[dict])
async def start_game():
    read_txt = read.read_num_errors(db_connection)
    return schemas.startGames_schema(read_txt)
