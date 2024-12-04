def read_start_game(conexion):
    conn = conexion
    cursor = conn.cursor()

    sql_read_tematica = ''' SELECT txt_comencar_partida FROM default_interface '''

    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchall()
    return result


def read_num_errors(conexion):
    conn = conexion
    cursor = conn.cursor()

    sql_read_tematica = ''' SELECT num_errors FROM partida '''

    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchall()
    return result
