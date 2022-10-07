nomes = list()
notas = []
numeros = list()
continuar = str
medias = list()
lista = [numeros, nomes, notas, medias]
numero = 0

while continuar != 'n':
    numeros.append(numero)
    nome = str(input('Nome: '))
    notaum = float(input('Nota 1: '))
    notadois = float(input('Nota 2: '))
    media = float((notaum + notadois) / 2)
    nomes.append(nome)
    notas.append(notaum)
    notas.append(notadois)
    medias.append(media)
    continuar = str(input('Deseja continuar [s/n]? ').lower())
    numero += 1

print('=' * 30)
print(f'{"BOLETIM DE NOTAS DOS ALUNOS":^}')
print('=' * 30)

for b in range(0, numero):
    if b == 0:
        print(f'{"Nº":<13}', end='')
        print(f'{"NOME":<13}', end='')
        print(f'{"MÉDIA":<10}', end='\n')

    print(f'{lista[0][b]:<10}', end='')
    print(f'{lista[1][b]:^10}', end='')
    print(f'{lista[3][b]:>10.1f}', end='\n')

continuar = 's'
while continuar != 'n':
    b = int(input('\nQual o nº do aluno? '))
    print(f'{lista[1][b]}: ', end='')
    if int(b % 2) == 0 or b == 0:
        print(f'{lista[2][b]} e {lista[2][b+1]}')
    else:
        print(f'{lista[2][b+1]} e {lista[2][b+2]}')

    continuar = str(input('Deseja continuar [s/n]? ').lower())
