c = str
nome = str
peso = float
qte = 0
maispes = list()
menospes = list()

while c != 'n':
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    qte += 1
    if peso > 72:
        maispes.append(nome)
    if peso < 72:
        menospes.append(nome)
    c = str(input('Deseja continuar [s/n]? ').lower())

print(f'Foram cadastradas {qte} pessoas.')

b = 0
print('Pessoas com mais de 72kg: ', end='')
for b in range(0, len(maispes)):
    print(f'{maispes[b]}...', end='')

b = 0
print('\nPessoas com menos de 72kg: ', end='')
for b in range(0, len(menospes)):
    print(f'{menospes[b]}...', end='')