def updateError(conexion):
    
    conn = conexion
    cursor = conn.cursor()
    
    query_updateErrors = ''' UPDATE partida set num_errors = num_errors + 1 where id_partida = 1'''
    
    cursor.execute(query_updateErrors)
    conn.commit()

    result = cursor.rowcount

    return result