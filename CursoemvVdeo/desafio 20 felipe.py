import random
a = input('primeiro: ')
b = input('segundo: ')
c = input('terceiro: ')
d = input('quarto: ')
lista = [a, b, c, d]
random.shuffle(lista)
print('ordem: {}'.format(lista))

