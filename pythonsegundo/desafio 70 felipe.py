nome = ''
preco = float
continuar = ''
menornome = ''
menor = float
cont = 1
soma = 0
maiores = 0
while continuar != 'n':
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    if cont == 1:
        menornome = nome
        menor = preco
    if preco < menor:
        menornome = nome
        menor = preco
    if preco > 1000.00:
        maiores += 1.0
    soma += preco
    while continuar != 'n' and continuar != 's':
        continuar = input('Deseja continuar [S/N]? ').strip().lower()
    if continuar == 'n':
        break
    continuar = ''
print(f'''\n
RESULTADOS:
A soma dos produtos é {soma:.2f}
{menornome} é o produto mais barato, custando R${menor:.2f}
{maiores} produtos custam mais de R$1000,00.''')