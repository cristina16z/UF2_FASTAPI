from connection import connection_db

def csv_to_db(pos,data):

    conn = connection_db()
    cur = conn.cursor()

    sql ='INSERT INTO paraules (paraules,tematica) VALUES (%s,%s);'

    values = ((data.get('WORD')[pos], data.get('THEME')[pos]))

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

    return {'Message':'Data inserted'}