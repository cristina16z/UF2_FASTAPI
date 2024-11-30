from fastapi import FastAPI
from typing import List
import random
# Importació dels Arxius
import insertDATA.connection as connection
import crud.read as read
import schemas.schemas as schemas




app = FastAPI()

db_connection = connection.connection_db()



# Ens retorni les 5 temàtiques

@app.get ("/penjat/tematica/opcions", response_model=List[dict])
async def read_tematicas():
    read_tematica = read.read_tematicas(db_connection)
    return schemas.tematicas_schema(read_tematica)



# Li pasem la tematica per a que retorni les 1 de les 100 paraules de la temàtica, de forma random

@app.get ("/penjat/tematica/{option}", response_model=List[dict])
async def read_paraula(option: str):
    read_words = read.read_word(db_connection, option)      # De totes les paraules
    random_word = random.choice(read_words)                 # Aleatoriament
    return schemas.paraules_schema(random_word)             # Escollim una




