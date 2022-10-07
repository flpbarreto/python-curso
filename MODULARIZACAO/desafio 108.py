from uteis import moeda


num = float(input('digite um numero: '))
print(f'{moeda.moeda(num)} mais 10% é {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'{moeda.moeda(num)} menos 5% é {moeda.moeda(moeda.diminuir(num, 5))}')
print(f'{moeda.moeda(num)} pela metade é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
