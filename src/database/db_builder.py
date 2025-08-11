# src/database/db_builder.py
import os
from src.database.db_connector import get_db_connection, close_db_connection

# Define o caminho para o arquivo de esquema SQL
SCHEMA_FILE_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def build_database():
    """
    Conecta ao banco de dados e executa o script SQL para criar as tabelas.
    Assume que o schema.sql contém comandos para DROPAR tabelas existentes
    e depois criá-las.
    """
    conn = None
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            with open(SCHEMA_FILE_PATH, 'r') as f:
                schema_sql = f.read()

            # Executa todos os comandos SQL do arquivo de esquema
            # O psycopg2 permite executar múltiplos comandos se separados por ;
            cursor.execute(schema_sql)
            conn.commit()
            print("Banco de dados construído/atualizado com sucesso!")
        else:
            print("Não foi possível estabelecer conexão com o banco de dados.")
    except Exception as e:
        if conn:
            conn.rollback() # Desfaz quaisquer alterações em caso de erro
        print(f"Erro ao construir o banco de dados: {e}")
    finally:
        if conn:
            close_db_connection(conn)

if __name__ == "__main__":
    print("Iniciando a construção do banco de dados...")
    build_database()
    print("Processo de construção do banco de dados concluído.")