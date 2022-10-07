import random
a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)
e = random.randint(0, 10)
tupla = (a, b, c, d, e)
cont = 0
maior = 0
menor = 0
for cont in range(0, 5, 1):
    if cont == 0:
        menor = tupla[cont]
        maior = tupla[cont]
    if maior < tupla[cont]:
        maior = tupla[cont]
    if menor > tupla[cont]:
        menor = tupla[cont]
    print(tupla[cont], end = ' ')
print(f'''\nO maior valor é {maior}
O menor valor é {menor}
--- FIM! ---''')