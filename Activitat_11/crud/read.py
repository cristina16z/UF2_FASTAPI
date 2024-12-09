def read_start_game(conexion):
    conn = conexion
    cursor = conn.cursor()

    sql_read_tematica = ''' SELECT txt_comencar_partida FROM default_interface where llenguatge = 'catala' '''

    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchone()
    return result


def read_num_errors(conexion):
    conn = conexion
    cursor = conn.cursor()

    sql_read_tematica = ''' SELECT num_errors FROM partida '''

    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchone()
    return result



def read_abecedari(conexion):
    conn = conexion
    cursor = conn.cursor()

    sql_read_tematica = ''' SELECT txt_abecedari FROM default_interface where llenguatge = 'catala' '''

    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchone()
    return result
     

def read_estadistiques_txt(conexion):
    conn = conexion
    cursor = conn.cursor()

    sql_read_tematica = ''' SELECT txt_punts_partides_actuals, txt_total_partides, txt_partides_guanyades, txt_partides_amb_mes_punts FROM default_interface where llenguatge = 'catala' '''

    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchone()
    return result



def read_estadistiques(conexion):
    conn = conexion
    cursor = conn.cursor()

    sql_read_tematica = ''' SELECT username, punts, total_partides, partides_guanyades, partides_amb_mes_punts from partida, jugador where partida.id_jugador = jugador.id '''

    cursor.execute(sql_read_tematica)
    conn.commit()
    result = cursor.fetchall()
    return result
