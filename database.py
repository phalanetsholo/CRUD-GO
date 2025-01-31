import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="Tsholofelo",
        user="postgres",  
        password="Oratile@22",  
        host="localhost",
        port="5433"
    )
    return conn
