from time import sleep

lista = list()
continuar = str
cadastro = dict()
mulheres = list()
total = 0
maiores = list()

while continuar != 'n':
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo [M/F]: ').lower())
    if cadastro['sexo'] == 'f':
        mulheres.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    total += cadastro['idade']
    lista.append(cadastro.copy())
    continuar = str(input('Deseja continuar [s/n]? ').lower())

media = float(total / (len(lista)))

for a in range(0, len(lista)):
    if lista[a]['idade'] > media:
        maiores.append(lista[a]['nome'])

print(f'\nForam cadastradas {len(lista)} pessoas.')
sleep(1)
print(f'A média das idades é {media:.1f} anos')

if len(mulheres) > 0:
    print(f'As mulheres são:', end=' ')
    sleep(1)
    for a in range(0, len(mulheres)):
        print(f'{mulheres[a]}', end=' ')
        sleep(1)

if len(maiores) > 0:
    print(f'\nAs pessoas com idade superior a média são:', end=' ')
    sleep(1)
    for a in range(0, len(maiores)):
        print(f'{maiores[a]}', end=' ')
        sleep(1)
