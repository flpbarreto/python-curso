import random
lista = [0, 1, 2, 3, 4, 5]
n = random.choice(lista)
num = int(input('digite um numero de 0 a 5: '))
if num == n:
    print('{} é igual a {}, você acertou'.format(n, num))
else:
    print('{} é diferente de {}, você errou'.format(n,num))
