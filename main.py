from system import module

module.l()
print(f'{"CADASTRO":^28}')
while True:
    module.l()
    print("""1 - Ver pessoas cadastradas
2 - Cadastrar Novas Pessoas
3 - Sair do Programa""")
    module.l()
    try:
        asnw = int(input('> Sua Opção: '))
        if asnw>3 or asnw<1:
            print('\033[31m[ERRO] Opção Inválida.\033[m')
    except ValueError:
        print('\033[31m[ERRO] Opção Inválida.\033[m')
        continue

    if asnw==1:
        module.l()
        module.show()
    elif asnw==2:
        module.l()
        module.add()
    elif asnw==3:
        module.l()
        print('\033[33mFIM DO PROGRAMA\033[m')
        break
