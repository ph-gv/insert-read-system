import sqlite3
from sqlite3 import Connection, Error

# Define o nome do arquivo do banco de dados (será criado na raiz do projeto)
DB_FILE = 'database.db'

def get_db_connection() -> Connection:
    """
    Tenta estabelecer e retornar a conexão com o banco de dados.
    Se o arquivo não existir, ele será criado.
    """
    connection = None
    try:
        # Abre a conexão (ou cria o arquivo DB_FILE se ele não existir)
        connection = sqlite3.connect(DB_FILE)
        return connection
    except Error as e:
        # Se houver um erro de conexão/arquivo, imprime e retorna None
        print(f"Erro ao conectar ao SQLite: {e}")
        return None


def create_tables(conn: Connection):
    """
    Cria a tabela 'Pessoas' se ela ainda não existir.
    """
    create_pessoas_table = """
    CREATE TABLE IF NOT EXISTS Pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_pessoas_table)
        conn.commit()
        print("Tabela 'Pessoas' verificada/criada com sucesso.")
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")


def initialize_db():
    """
    Função principal para inicializar o banco de dados.
    """
    conn = get_db_connection()
    if conn:
        create_tables(conn)
        conn.close()
        return True
    return False
