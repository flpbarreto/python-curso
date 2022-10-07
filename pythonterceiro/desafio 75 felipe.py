n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
tupla = (n1, n2, n3, n4)
contador = 0
for c in range(0, 4, 1):
    if tupla[c] == 9:
        contador += 1
    if c == 0 :
        print('Os valores pares são:', end = '\n')
    if tupla[c] % 2 == 0:
        print(tupla[c], end = ' ')
if 3 in tupla:
    tres = tupla.index(3)
    print(f'\nO valor 3 foi digitado pela primeira vez na {tres + 1}ª posição.')
print(f'O valor 9 apareceu {contador} vezes')
