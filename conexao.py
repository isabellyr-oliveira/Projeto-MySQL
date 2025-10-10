import mysql.connector
#pip install mysql-connector-python
from dotenv import load_dotenv
#pip install dotenv
import os
#carregar asv variaveis de ambiente (.env)
load_dotenv()

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conexao.cursor()
        print(f"Conexão estabelecida: {conexao}")
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexão: {erro}")
        return None, None
