lista = list()
pares = list()
impares = list()
c = str
num = int
cont = int
teste = int

while c != 'n':
    num = input('Digite um valor inteiro: ')
    lista.append(num)
    c = str(input('Deseja continuar [s/n]? ').lower())

for cont in range(0, len(lista)):
    num = int(lista[cont])
    if (int(num % 2) == 0):
        pares.append(num)
    else:
        impares.append(num)

print(f'Lista: {lista}\nPares: {pares}\nÍmpares: {impares}')
