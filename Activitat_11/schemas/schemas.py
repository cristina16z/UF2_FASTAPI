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
    return {'username':frase}


def estadistiques_schemas(frases) -> dict:
    return [estadistiques_schema(frase) for frase in frases]




