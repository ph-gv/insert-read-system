import customtkinter as ctk
from dao.pessoa_dao import PessoaDAO
from model.pessoa_model import Pessoa
from view.add_person_view import AddPersonView

# Configurações globais de aparência
ctk.set_appearance_mode("System")  # Segue o tema do Windows/macOS
ctk.set_default_color_theme("blue")

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.dao = PessoaDAO()
        self.title("Sistema de Cadastro")
        self.geometry("600x450")

        # Configuração de Grid (Layout Manager - similar ao GridBagLayout)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- Cabeçalho ---
        self.label_titulo = ctk.CTkLabel(self, text="Pessoas Cadastradas", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.grid(row=0, column=0, padx=20, pady=20)

        # --- Lista de Pessoas (Equivalente ao JList/JTable em ScrollPane) ---
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Registros")
        self.scrollable_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # --- Botões de Ação ---
        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.btn_add = ctk.CTkButton(self.btn_frame, text="Novo Cadastro", command=self.abrir_cadastro)
        self.btn_add.pack(side="left", padx=10, pady=10, expand=True)

        self.btn_refresh = ctk.CTkButton(self.btn_frame, text="Atualizar Lista", command=self.atualizar_lista)
        self.btn_refresh.pack(side="left", padx=10, pady=10, expand=True)

        # Inicializa a lista
        self.atualizar_lista()

    def abrir_cadastro(self):
        # Abre a janela de cadastro passando 'self' como pai
        AddPersonView(self)

    def atualizar_lista(self):
        """Limpa o frame e busca dados atualizados do DAO."""
        # Limpa widgets existentes (Equivalente ao removeAll do Java)
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        pessoas = self.dao.read_all()
        
        if not pessoas:
            label = ctk.CTkLabel(self.scrollable_frame, text="Nenhum registro encontrado.")
            label.grid(row=0, column=0, pady=10)

        for i, pessoa in enumerate(pessoas):
            # Cria um "card" para cada pessoa
            item_text = f"ID: {pessoa.id} | {pessoa.nome} ({pessoa.idade} anos)"
            
            # Label da Pessoa
            label = ctk.CTkLabel(self.scrollable_frame, text=item_text, anchor="w")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            # Botão Deletar (Função inline usando lambda para passar o ID)
            btn_del = ctk.CTkButton(self.scrollable_frame, text="Excluir", width=60, 
                                    fg_color="red", hover_color="#8B0000",
                                    command=lambda p=pessoa: self.confirmar_exclusao(p))
            btn_del.grid(row=i, column=1, padx=10, pady=5)

    def confirmar_exclusao(self, pessoa):
        if self.dao.delete(pessoa.id):
            print(f"Pessoa {pessoa.nome} excluída!")
            self.atualizar_lista()
