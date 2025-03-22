import json

def show() -> str:
    """
    -->Exibe lista de cadastrados ao usuário.
    """
# TENTA EXIBIR O ARQUIVO AO USUARIO
    try:
        with open('dados.json', 'r') as file:
            people = json.load(file)
        if not people:
            print('Nenhuma pessoa cadastrada.')
        else:
            print(f'{"Pessoas Cadastradas":^52}')
            for person in people:
                print(f'Nome: {person["nome"]:<18} {'|':<5} Idade: {person["idade"]}')
# EXCEÇÕES
    except FileNotFoundError:
        print('\033[31mO arquivo não foi encontrado.\033[m')


def add() -> str:
    """
    -->Adiciona e salva dados em uma lista.
    """
# COLHE DADOS DO USUÁRIO
    while True:
        name = str(input('Nome: '))
        bool_name = validate_name(name)
        if bool_name==True:
            break

    while True:        
        age = input('Idade: ').strip()
        bool_age = validate_age(age)
        if bool_age==True:
            break
    
    new_person = {'nome':name, 'idade':age}
# TENTA ABRIR O ARQUIVO E CARREGAR DADOS RECENTES
    try: 
        with open('dados.json', 'r') as file:   
            people = json.load(file)
    except FileNotFoundError:  
        people = list()
# ADICIONA OS DADOS A UMA LISTA DENTRO DE UMA CHAVE
    people.append(new_person)
# SALVA OS DADOS PRESENTES NO ARQUIVO
    with open('dados.json', 'w') as file:
        json.dump(people, file, indent=4)
    print(f'\033[32m{name} cadastrado com sucesso!\033[m')


def validate_name(name) -> bool:
    """
    -->Verifica se o valor digitado pelo usuário é válido.
    """
    name.strip()
    if all(c.isalpha() or c.isspace() for c in name):
        return True
    else:
        print('\033[31m[ERRO] Digite dados válidos.\033[m')
        l()
        return False


def validate_age(age) -> bool:
    """
    -->Verifica se o valor digitado pelo usuário é válido.
    """
    if age.isdigit():
        return True
    else:
        print('\033[31m[ERRO] Digite dados válidos.\033[m')
        l()
        return False


def l() -> str:
    print('---'*10)
