a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))
valores = (a, b, c, d)
tres = 0
nove = 0
for cont in range(0, 4):
    if valores[cont] == 9:
        nove += 1
    if tres == 0 and valores[cont] == 3:
        tres += 1
        posicao = cont + 1
if nove != 0:
    print(f'O valor 9 apareceu {nove} vezes')
if nove == 0:
    print('O valor 9 apareceu 0 vezes')
if tres != 0:
    print(f'O valor 3 apareceu pela primeira vez na '
      f'{posicao}ª posição')
if tres == 0:
    print('O valor 3 não foi digitado em nenhuma '
          'posição.')
cont = 0
print('Os valores pares são:')
for cont in range(0, 4):
    if valores[cont] % 2 == 0:
        print(valores[cont])
