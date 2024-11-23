def read(conn):
    conn = conn
    cursor = conn.cursor()

    sql_read = ''' SELECT * FROM users'''

    cursor.execute(sql_read)
    conn.commit()

    result = cursor.fetchall()

    return result