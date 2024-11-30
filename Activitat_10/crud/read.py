def read_tematicas(conexion):
    conn = conexion
    cursor = conn.cursor()

    # De la columna tematica, seleccionem totes les temàticas úniques, sense repetir, que són 5
    sql_read_tematica = ''' SELECT distinct tematica FROM paraules'''
    
    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchall()
    return result



def read_word(conexion, tema):
    conn = conexion
    cursor = conn.cursor()

    # De la columna paraula, seleccionem totes les que coincideixin amb la temàtica
    sql_read_paraula = ''' SELECT paraula FROM paraules where tematica = %s '''
    
    cursor.execute(sql_read_paraula, (tema.upper(),))
    conn.commit()
    result = cursor.fetchall()
    return result