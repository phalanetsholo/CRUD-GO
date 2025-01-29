import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="employee_db",
        user="postgres",  # Replace with your PostgreSQL username
        password="Oratile@22",  # Replace with your PostgreSQL password
        host="localhost",
        port="5433"
    )
    return conn