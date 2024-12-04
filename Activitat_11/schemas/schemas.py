def startGame_schema(frase) -> dict:
    return {'text':frase}


def numErros_schema(frase) -> dict:
    return {'número errors' :frase}



def startGames_schema(frases) -> dict:
    return [startGame_schema(frase) for frase in frases]
