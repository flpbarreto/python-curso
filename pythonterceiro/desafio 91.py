import random
import time
import operator

jogadores = dict()

jogadores['Jogador 1'] = random.randint(1, 6)
jogadores['Jogador 2'] = random.randint(1, 6)
jogadores['Jogador 3'] = random.randint(1, 6)
jogadores['Jogador 4'] = random.randint(1, 6)

for j, v in jogadores.items():
    print(f'{j}: {v}')
    time.sleep(1)

ranking = sorted(jogadores.items(),
                 key = operator.itemgetter(1),
                 reverse=True)

lugar = 1
for j, v in enumerate(ranking):
    print(f'{lugar}º: {v[0]} que tirou {v[1]}')
    lugar += 1
    time.sleep(1)
