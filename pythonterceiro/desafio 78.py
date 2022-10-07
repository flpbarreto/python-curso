lista = list()
indmaior = list()
indmenor = list()
maior = int
menor = int
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = lista[c]
        maior = lista[c]

c = 0
for c in range(0, 5):
    if lista[c] >= maior:
        if lista[c] > maior:
            indmaior = []
            indmaior.append(c)
        if lista[c] == maior:
            indmaior.append(c)
        maior = lista[c]
    if lista[c] <= menor:
        if lista[c] < menor:
            indmenor = []
            indmenor.append(c)
        if lista[c] == menor:
            indmenor.append(c)
        menor = lista[c]

c = 0
print(f'o maior valor é {maior} que aparece nas'
      f' posições', end=' ')
for c in indmaior:
    print(f'{c}...', end='')
print(f'\no menor valor é {menor} que aparece nas'
      f' posições', end=' ')
for c in indmenor:
    print(f'{c}...', end='')
