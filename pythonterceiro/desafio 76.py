listagem = ('Lápis', 1.75, 'Borracha', 2.00,
            'Caderno', 15.00, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
c = 0
cont = 1
while True:
    print(f'{listagem[c]:.<30}R${listagem[cont]:>7.2f}')
    c += 2
    cont += 2
    if c >= len(listagem):
        break
