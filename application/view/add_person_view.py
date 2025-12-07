import customtkinter as ctk
from model.pessoa_model import Pessoa
from dao.pessoa_dao import PessoaDAO

class AddPersonView(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent # Referência à MainView para atualizar a lista depois
        self.dao = PessoaDAO()
        
        self.title("Novo Cadastro")
        self.geometry("300x250")
        self.grab_set()  # Torna a janela modal (foca apenas nela)

        # Labels e Inputs
        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack(pady=(20, 0))
        self.entry_nome = ctk.CTkEntry(self)
        self.entry_nome.pack(pady=5)

        self.label_idade = ctk.CTkLabel(self, text="Idade:")
        self.label_idade.pack(pady=(10, 0))
        self.entry_idade = ctk.CTkEntry(self)
        self.entry_idade.pack(pady=5)

        # Botão Salvar
        self.btn_salvar = ctk.CTkButton(self, text="Salvar", command=self.salvar)
        self.btn_salvar.pack(pady=20)

    def salvar(self):
        nome = self.entry_nome.get()
        try:
            idade = int(self.entry_idade.get())
            # Cria o objeto Model
            nova_pessoa = Pessoa(nome=nome, idade=idade)
            
            # Persiste via DAO
            if self.dao.create(nova_pessoa):
                print("Salvo com sucesso!")
                self.parent.atualizar_lista() # Callback para atualizar a tela principal
                self.destroy() # Fecha a janela
        except ValueError as e:
            print(f"Erro nos dados: {e}")
