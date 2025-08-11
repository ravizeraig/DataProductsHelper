# src/config/settings.py
import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

# Variáveis de ambiente para o banco de dados
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "data_products_db") # Nome que daremos ao nosso DB
DB_USER = os.getenv("DB_USER", "postgres") # Geralmente o usuário padrão do PostgreSQL
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres") # Sua senha do PostgreSQL
DB_PORT = os.getenv("DB_PORT", "5432")

# --- Linha para depuração temporária ---
print(f"DEBUG: Carregada senha: {DB_PASSWORD}") # REMOVA ESSA LINHA DEPOIS DE DEPURAR!
# --- Fim da linha para depuração ---