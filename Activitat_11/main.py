from fastapi import FastAPI
from typing import List
import insertData.connection as connection
import schemas.schemas as schemas
import crud.read as read
import crud.update as update



app = FastAPI()
db_connection = connection.connection_db()

# Extreure el text de començar partida
@app.get ("/start-game", response_model=List[dict])
async def start_game():
    read_txt = read.read_start_game(db_connection)
    return schemas.startGames_schema(read_txt)


# Enviar un increment d'errors
@app.post("/start-game/errors/augment-errors/")
async def augment_errors():
    result = update.updateError(db_connection)
    return result


# Recollir de la BDD el núm d'errors
@app.get ("/start-game/errors/num-errors", response_model=List[dict])
async def num_errors():
    read_txt = read.read_num_errors(db_connection)
    return schemas.gameErrors_schema(read_txt)


# Extreure les lletres del abecedari
@app.get ("/start-game/abecedari", response_model=List[dict])
async def abecedari():
    read_txt = read.read_abecedari(db_connection)
    return schemas.startGames_schema(read_txt)


# Extreure el text default de les estadístiques
@app.get ("/start-game/estadistiques/text", response_model=List[dict])
async def estadistiques_text():
    read_txt = read.read_estadistiques_txt(db_connection)
    return schemas.startGames_schema(read_txt)


# Extracció dades estadístiques 

@app.get ("/start-game/estadistiques/puntuacio", response_model=List[dict])
async def estadistiques():
    read_txt = read.read_estadistiques(db_connection)
    return schemas.estadistiques_schemas(read_txt)