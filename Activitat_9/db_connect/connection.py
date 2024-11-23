import psycopg2


def connection_db():
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='cristina',
            password='system',
            host='localhost',
            port='5432'
        )

        print(f'Conexió establerta correctament: {connection_db}')

        return conn

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        pass