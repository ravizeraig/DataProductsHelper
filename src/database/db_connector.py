# src/database/db_connector.py
import psycopg2
from src.config.settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

def get_db_connection():
    """
    Estabelece e retorna uma conexão com o banco de dados PostgreSQL.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def close_db_connection(conn):
    """
    Fecha a conexão com o banco de dados.
    """
    if conn:
        conn.close()