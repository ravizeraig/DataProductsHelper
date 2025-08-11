# src/test_connection.py

from src.database.db_connector import get_db_connection, close_db_connection

def test_connection():
    print("Tentando conectar ao banco de dados...")
    conn = get_db_connection()
    if conn:
        print("Conexão com o banco de dados estabelecida com sucesso!")
        try:
            # Opcional: Executar uma consulta simples para testar
            cursor = conn.cursor()
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print(f"Versão do PostgreSQL: {db_version[0]}")

            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
            tables = cursor.fetchall()
            print("\nTabelas existentes no banco de dados:")
            for table in tables:
                print(f"- {table[0]}")

            cursor.close()
        except Exception as e:
            print(f"Erro ao executar consulta de teste: {e}")
        finally:
            close_db_connection(conn)
            print("Conexão com o banco de dados fechada.")
    else:
        print("Falha ao estabelecer conexão com o banco de dados.")

if __name__ == "__main__":
    test_connection()