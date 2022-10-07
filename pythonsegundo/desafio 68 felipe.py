import random
escolha = ''
jogador = computador = int
resultado = 1
cont = 0
while resultado == 1:
    jogador = int(input('Digite um número: '))
    while escolha != 'p' and escolha != 'i':
        escolha = str(input('Par ou ímpar [P/I]? ')).strip().lower()
    computador = random.randint(0, 10)
    soma = computador + jogador
    if (soma % 2) == 0:
        if escolha == 'p':
            resultado = 1
            cont += 1
            print(f'Você ganhou! Eu escolhi {computador}.')
        else:
            resultado = 0
            print(f'Você perdeu! Eu escolhi {computador}.')
    if (soma % 2) != 0:
        if escolha == 'i':
            resultado = 1
            cont +=1
            print(f'Você ganhou! Eu escolhi {computador}.')
        else:
            resultado = 0
            print(f'Você perdeu! Eu escolhi {computador}.')
print(f'Você ganhou {cont} vezes seguidas.')
