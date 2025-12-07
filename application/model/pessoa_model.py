from dataclasses import dataclass
from typing import Optional

# O decorator @dataclass gera automaticamente:
# - O construtor (__init__)
# - O método de representação para printar o objeto (__repr__)
# - Métodos de comparação (__eq__)
@dataclass
class Pessoa:
    """
    Define o modelo de objeto Pessoa.
    Equivalente a um POJO (Plain Old Java Object) com getters e setters implícitos.
    """
    
    nome: str
    idade: int
    
    # ID é opcional (Optional[int]) porque ele só existirá APÓS ser salvo no banco, 
    # já que o SQLite gera o ID automaticamente (AUTOINCREMENT).
    id: Optional[int] = None 
    
    
    def __post_init__(self):
        """
        Método executado após o __init__. 
        Podemos usá-lo para fazer validações básicas.
        """
        if not isinstance(self.idade, int) or self.idade < 0:
            raise ValueError("Idade deve ser um número inteiro positivo.")
        if not self.nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        