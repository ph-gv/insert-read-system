from sqlite3 import Connection
from typing import List, Optional

# Importando o modelo de dados e o utilitário de conexão
from model.pessoa_model import Pessoa
from util.db_connector import get_db_connection 


class PessoaDAO:
    """
    Data Access Object para o modelo Pessoa.
    Responsável por todas as operações de CRUD no banco SQLite.
    """

    def __init__(self):
        """Inicializa o DAO e garante que a conexão será fechada externamente."""
        pass

    # ------------------------------------
    # 1. CREATE (Cadastrar Nova Pessoa)
    # ------------------------------------
    def create(self, pessoa: Pessoa) -> Optional[Pessoa]:
        """Insere uma nova pessoa no banco de dados e retorna o objeto com o ID gerado."""
        conn: Connection = get_db_connection()
        if not conn:
            return None

        # O ID é gerado automaticamente pelo SQLite (AUTOINCREMENT)
        sql = "INSERT INTO Pessoas (nome, idade) VALUES (?, ?)"
        
        try:
            cursor = conn.cursor()
            # O cursor.execute recebe os parâmetros em uma tupla para evitar SQL Injection
            cursor.execute(sql, (pessoa.nome, pessoa.idade))
            conn.commit()
            
            # Recupera o ID gerado automaticamente pela última inserção
            pessoa.id = cursor.lastrowid 
            return pessoa
            
        except Exception as e:
            print(f"Erro ao criar Pessoa: {e}")
            conn.rollback()
            return None
            
        finally:
            conn.close()

    # ------------------------------------
    # 2. READ ALL (Listar Todas)
    # ------------------------------------
    def read_all(self) -> List[Pessoa]:
        """Retorna uma lista de todos os objetos Pessoa no banco de dados."""
        conn: Connection = get_db_connection()
        if not conn:
            return []

        sql = "SELECT id, nome, idade FROM Pessoas"
        pessoas: List[Pessoa] = []

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            # Mapeamento do ResultSet (rows) para a lista de objetos Pessoa (POJOs)
            for row in rows:
                # row[0] é o id, row[1] é o nome, row[2] é a idade
                pessoa = Pessoa(id=row[0], nome=row[1], idade=row[2])
                pessoas.append(pessoa)
                
            return pessoas

        except Exception as e:
            print(f"Erro ao ler todas as Pessoas: {e}")
            return []
            
        finally:
            conn.close()
            
    # ------------------------------------
    # 3. READ SINGLE (Buscar por ID)
    # ------------------------------------
    def read_by_id(self, person_id: int) -> Optional[Pessoa]:
        """Retorna uma pessoa específica pelo ID."""
        conn: Connection = get_db_connection()
        if not conn:
            return None

        sql = "SELECT id, nome, idade FROM Pessoas WHERE id = ?"
        
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (person_id,)) # O parâmetro deve ser uma tupla
            row = cursor.fetchone()

            if row:
                # Retorna o objeto Pessoa mapeado
                return Pessoa(id=row[0], nome=row[1], idade=row[2])
            else:
                return None # Não encontrado

        except Exception as e:
            print(f"Erro ao ler Pessoa por ID: {e}")
            return None
            
        finally:
            conn.close()

    # ------------------------------------
    # 4. UPDATE (Atualizar Dados Existentes)
    # ------------------------------------
    def update(self, pessoa: Pessoa) -> bool:
        """Atualiza os dados de uma pessoa no banco com base no ID."""
        if pessoa.id is None:
            return False

        conn: Connection = get_db_connection()
        if not conn:
            return False

        sql = "UPDATE Pessoas SET nome = ?, idade = ? WHERE id = ?"
        
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (pessoa.nome, pessoa.idade, pessoa.id))
            conn.commit()
            
            # Verifica se alguma linha foi de fato alterada
            return cursor.rowcount > 0
            
        except Exception as e:
            print(f"Erro ao atualizar Pessoa: {e}")
            conn.rollback()
            return False
            
        finally:
            conn.close()

    # ------------------------------------
    # 5. DELETE (Remover Registro)
    # ------------------------------------
    def delete(self, person_id: int) -> bool:
        """Remove uma pessoa do banco de dados pelo ID."""
        conn: Connection = get_db_connection()
        if not conn:
            return False

        sql = "DELETE FROM Pessoas WHERE id = ?"
        
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (person_id,))
            conn.commit()
            
            # Retorna True se um registro foi deletado
            return cursor.rowcount > 0

        except Exception as e:
            print(f"Erro ao deletar Pessoa: {e}")
            conn.rollback()
            return False
            
        finally:
            conn.close()
            