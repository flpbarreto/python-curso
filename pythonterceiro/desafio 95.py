from time import sleep

qtde = list()
jogadores = list()
continuar = str
gols = int

while continuar != 'n':

    golstotal = 0

    cadastro = {'nome': str(input('Qual o nome do jogador? ')),
            'partidas': int(input('Quantas partidas foram jogadas? '))}


    for a in range(0, cadastro['partidas']):
        gols = int(input(f'Quantos gols foram feitos na partida {a+1}? '))
        qtde.append(gols)
        golstotal += gols
    cadastro['gols por partida'] = qtde[:]
    cadastro['total de gols'] = golstotal
    jogadores.append(cadastro.copy())
    qtde.clear()
    continuar = str(input('Deseja continuar [s/n]? '))
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Deseja continuar [s/n]? '))

print('=' * 30)
print(f'{"CÓD":<8}{"NOME":<8}{"GOLS":^8}{"TOTAL":>5}')
print('=' * 30, end='\n')


for a in range(0, len(jogadores)):
    print(f'\n{a:<8}', end='')
    print(f'{jogadores[a]["nome"]:<8}', end='')
    print(f'{jogadores[a]["gols por partida"]}', end='')
    print(f'{jogadores[a]["total de gols"]:>8}')
    sleep(1)

print('-' * 30)

c = int
while True:
    c = int(input('Mostrar dados de qual jogador [999 interrompe]? '))
    while c != 999 and c > (len(jogadores) - 1) or c < 0:
        print(f'ERRO! Não exite o jogador {c} Tente novamente.')
        c = int(input('Mostrar dados de qual jogador [999 interrompe]? '))
    if c == 999:
        break
    print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[c]["nome"]}:')
    sleep(1)
    for a in range(0, len(jogadores[c]["gols por partida"])):
        print(f'No jogo {a+1} fez {jogadores[c]["gols por partida"][a]}')
        sleep(1)
    print('-' * 30)
