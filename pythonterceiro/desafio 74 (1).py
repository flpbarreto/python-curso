import random
a = random.random()
b = random.random()
c = random.random()
d = random.random()
e = random.random()
valores = (a, b, c, d, e)
for c in range(0, 5):
    print(valores[c])
menor = valores[0]
maior = valores[0]
for c in range(1, 5):
    if valores[c] > maior:
        maior = valores[c]
    if valores[c] < menor:
        menor = valores[c]
print(f'O maior valor é {maior}\n'
      f'O menor valor é {menor}')
