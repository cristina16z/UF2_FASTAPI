def tema_schema(tema) -> dict:                              # Retorna un diccionari
    return {"tematica": tema}                               # De clau "tematica" amb el valor que li passem

def tematicas_schema(tematicas) -> dict:                    # El [0] se toma el primer valor, que sólo contiene la cadena de txt,
    return [tema_schema(tema[0]) for tema in tematicas]     # ya que sino saldria [txt]


def word_schema(paraula) -> dict:
    return {"paraula": paraula}

def paraules_schema(paraules) -> dict:                       # Toma una lista y las transforma en una lista de diccionarios
    return [word_schema(paraula) for paraula in paraules]