from time import sleep
while True:
    print(f'\033[0;30;43m~' * 30)
    print(f'\033[0;30;43m{"   Sistema de ajuda PyHELP":^}')
    print(f'\033[0;30;43m~' * 30)
    sleep(1)
    funcao = str(input('\033[mDigite a função que deseja ajuda: '))
    qtde = len(funcao)
    print(f'\033[0;30;46m~' * (36 + qtde))
    print(f"   Acessando o manual de comando '{funcao}':   ")
    print(f'~' * (36 + qtde))
    print('\033[m')
    sleep(1)
    help(funcao)