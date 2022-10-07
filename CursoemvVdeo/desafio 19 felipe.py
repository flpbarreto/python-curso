import random
a = input('digite primeiro nome: ')
b = input('digite segundo nome: ')
c = input('digite terceiro nome: ')
d = input('quarto: ')
lista = [a, b, c, d]
escolhido = random.choice(lista)
print('o escolhido é {}'.format(escolhido))
