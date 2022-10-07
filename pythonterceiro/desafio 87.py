linhazero = list()
linhaum = list()
linhadois = list()
pares = 0
colunatres = 0
maior = int

coluna = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [0, {coluna}]: '))
    if int(num % 2) == 0:
        pares += num
    if coluna == 2:
        colunatres += num
    linhazero.append(num)
    coluna += 1

coluna = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [1, {coluna}]: '))
    if int(num % 2) == 0:
        pares += num
    if coluna == 2:
        colunatres += num
    if c == 0 or num > maior:
        maior = num
    linhaum.append(num)
    coluna += 1

coluna = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [2, {coluna}]: '))
    if int(num % 2) == 0:
        pares += num
    if coluna == 2:
        colunatres += num
    linhadois.append(num)
    coluna += 1

for c in range(0, 3):
    print(f'[ {linhazero[c]} ]', end=' ')

for c in range(0, 3):
    if c == 0:
        print(f'\n[ {linhaum[c]} ]', end=' ')
    else:
        print(f'[ {linhaum[c]} ]', end=' ')

for c in range(0, 3):
    if c == 0:
        print(f'\n[ {linhadois[c]} ]', end=' ')
    else:
        print(f'[ {linhadois[c]} ]', end=' ')

print(f'\n\nA soma dos valores pares é {pares}')

print(f'A soma dos itens da 3ª coluna é {colunatres}')

print(f'O maior valor da segunda linha é {maior}')
