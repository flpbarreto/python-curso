lista = list()
num = int
c = str

while c != 'n':
    num = int(input('Digite um número: '))
    if num in lista:
        c = str(input('Quer continuar [S/N]? ').lower())
    else:
        lista.append(num)
        c = str(input('Quer continuar [S/N]? ').lower())

lista.sort()
print(lista)
