from uteis import moeda


num = int(input('digite um numero: '))
print(f'{num} mais 10% é {moeda.aumentar(num, 10)}')
print(f'{num} menos 5% é {moeda.diminuir(num, 5)}')
print(f'{num} pela metade é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
