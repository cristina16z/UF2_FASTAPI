def startGame_schema(frase) -> dict:
    return {'text':frase}            

def startGames_schema(frases) -> dict:
    return [startGame_schema(frase) for frase in frases]



# Esquema dels errors

def numError_schema(frase) -> dict:
    return {'número errors':frase}

def gameErrors_schema(frases) -> dict:
    return [numError_schema(frase) for frase in frases]



# Esquemes de les estadístiques

def estadistiques_schema(frase) -> dict:
    return {'username':frase[0],
            'punts':frase[1],
            'total_partides': frase[2],
            'partides_guanyades':frase[3],
            'partida_amb_mes_punts':frase[4],
            'data_partida_millor_puntuacio':frase[5]
            }


def estadistiques_schemas(frases) -> dict:
    return [estadistiques_schema(frase) for frase in frases]




