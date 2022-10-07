from time import sleep

qtde = []
cadastro = {'nome': str(input('Qual o nome do jogador? ')),
            'partidas': int(input('Quantas partidas foram jogadas? ')),
            'gol por partida': qtde}
golstotal = 0

for a in range(0, cadastro['partidas']):
    gols = int(input(f'Quantos gols foram feitos na partida {a+1}? '))
    qtde.append(gols)
    golstotal += gols

print(f'\nO jogador {cadastro["nome"]} jogou {cadastro["partidas"]} partidas.')
sleep(1)

for a in range(0, cadastro["partidas"]):
    print(f'Na partida {a+1}, fez {qtde[a]} gols.')
    sleep(1)

print(f'Foi um total de {golstotal} gols.')
