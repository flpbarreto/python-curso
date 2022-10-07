lista = str(input('Digite a expressão: '))
qtde = lista.count('(') + lista.count(')')

if qtde == 0 or int(qtde % 2) == 0:
    print('A expressão é válida')
else:
    print('A expressão não é válida')
