pares = list()
impares = list()
lista = [pares, impares]

for c in range(0, 7):
    num = int(input('Digite um valor: '))
    if int(num % 2) == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()

print(f'Os pares são {pares}')
print(f'Os ímpares são {impares}')