linhazero = list()
linhaum = list()
linhadois = list()

coluna = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [0, {coluna}]: '))
    linhazero.append(num)
    coluna += 1

coluna = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [1, {coluna}]: '))
    linhaum.append(num)
    coluna += 1

coluna = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [2, {coluna}]: '))
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
