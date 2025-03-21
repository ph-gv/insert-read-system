# Insert & Read System
 **PT-BR**
🔍 **Descrição**
 - Sistema de Cadastro de Pessoas via linha de comando, desenvolvido em Python.

✨ **Funcionalidades**
 - Visualizar Pessoas Cadastradas
 - Cadastrar Novas Pessoas
 - Validação de Nome e Idade
 - Armazenamento em JSON para persistência dos dados

🛠️ **Tecnologias Utilizadas**
 - Python 3.12.8

📚 **Bibliotecas**
 - json (para manipulação de arquivos JSON)

🏗️ **Estrutura do Código**
Importação de Bibliotecas:
 - Usa o módulo json para manipulação de arquivos e armazenamento dos dados.

Funções Principais:
 - show(): Exibe a lista de pessoas cadastradas.
 - add(): Adiciona uma nova pessoa ao sistema, validando nome e idade.
 - validate_name(name): Garante que o nome contenha apenas letras e espaços.
 - validate_age(age): Verifica se a idade informada é um valor numérico.
 - l(): Exibe um separador visual para organização no terminal.

Interface de Linha de Comando:
 - Exibe um menu interativo para escolha das opções.
 - Permite ao usuário visualizar e adicionar cadastros facilmente.
 - Apresenta mensagens de erro para entradas inválidas.

 **EN-US**

🔍 **Description**
 - Command-line People Registration System, developed in Python.

✨ **Features**
 - View Registered People
 - Register New People
 - Name and Age Validation
 - JSON Storage for Data Persistence

🛠️ **Technology**
 - Python 3.12.8

📚 **Library**
 - json (for handling JSON files)

🏗️ **Code Structure**
Library Import:
 - Uses the json module to handle files and store data.

Main Functions:
 - show(): Displays the list of registered people.
 - add(): Adds a new person to the system, validating name and age.
 - validate_name(name): Ensures the name contains only letters and spaces.
 - validate_age(age): Checks if the given age is a numeric value.
 - l(): Displays a visual separator for terminal organization.

Command-Line Interface:
 - Displays an interactive menu for option selection.
 - Allows users to easily view and add registrations.
 - Shows error messages for invalid inputs.