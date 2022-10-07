valores = list()
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))

for c, b in enumerate(valores):
    print(f'Na posição {c} está {b}.')

print('FINISHED!')