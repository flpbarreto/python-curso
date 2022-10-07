import random
print('=' * 30)

jogos = int(input('Quantos jogos deseja criar? '))
lista = list()

for cont in range(1, (jogos + 1)):
    for c in range(0, 6):
        num = random.randint(1, 60)
        while num in lista:
            num = random.randint(1, 60)
        lista.append(num)
        if c == 5:
            print(f'Jogo {cont}: {lista}')
    lista.clear()
