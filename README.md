# 🗂️ Sistema de Cadastro CRUD - Python & CustomTkinter

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)](https://www.sqlite.org/)
[![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-darkgreen.svg)](https://github.com/TomSchimansky/CustomTkinter)

## 📌 Sobre o Projeto
Este projeto consiste em um sistema **CRUD** (Create, Read, Update, Delete) evolutivo. Originalmente concebido como um script CLI simples, foi refatorado para uma arquitetura moderna baseada em **MVC (Model-View-Controller)** e **DAO (Data Access Object)**, utilizando **SQLite** para persistência e **CustomTkinter** para uma interface gráfica intuitiva e responsiva.

O foco principal foi o desacoplamento de lógica e a aplicação de boas práticas de Engenharia de Software aprendidas anteriormente com Java/Swing.

## 🏗️ Arquitetura e Estrutura de Pastas
O projeto é organizado em módulos para garantir a separação de responsabilidades:

```text
insert-read-system/
├── app.py                  # Ponto de entrada (Entry Point)
├── database.db             # Banco de dados SQLite
├── model/
│   └── pessoa_model.py     # POJO (Plain Old Java Object) com Dataclasses
├── dao/
│   └── pessoa_dao.py       # Camada de Persistência (SQL)
├── util/
│   └── db_connector.py     # Gerenciamento de Conexão e Tabelas
└── view/
    ├── main_view.py        # Janela Principal
    └── add_person_view.py  # Janela de Formulário Modal
````

## 🚀 Funcionalidades Atuais

  - [x] Interface moderna com suporte nativo a temas (Claro/Escuro).
  - [x] Listagem dinâmica de usuários via `ScrollableFrame`.
  - [x] Cadastro de novos usuários através de janelas modais (`CTkToplevel`).
  - [x] Exclusão direta de registros com atualização de interface reativa.
  - [x] Validação de dados (tipagem de idade e campos não vazios).

## 🛠️ Tecnologias Utilizadas

  - **Linguagem:** Python 3.12+
  - **Interface Gráfica:** CustomTkinter (Extensão moderna do Tkinter)
  - **Banco de Dados:** SQLite3
  - **Mapeamento de Dados:** Python Dataclasses

## 🔧 Como Executar

1.  Instale a biblioteca necessária:
    ```bash
    pip install customtkinter
    ```
2.  Execute a aplicação a partir da raiz:
    ```bash
    python app.py
    ```

## 📈 Roadmap (Futuras Implementações)

  - [ ] Implementar edição de registros existentes (Update).
  - [ ] Adicionar pop-ups de confirmação (Dialogs) para ações críticas.
  - [ ] Criar sistema de filtro/busca dinâmica por nome.
  - [ ] Implementar exportação de relatórios (CSV/PDF).

-----

Desenvolvido como projeto de aprimoramento individual em Python e Engenharia de Software.