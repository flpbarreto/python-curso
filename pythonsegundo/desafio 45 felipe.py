import random
lista = ['tesoura', 'papel', 'pedra']
jogo = random.choice(lista)
humano = input('pedra, papel ou tesoura? ').strip()
humano = humano.lower()
if humano == 'tesoura' and jogo == 'papel':
    print('Você ganhou!!! Escolhi papel.')
elif humano == 'papel' and jogo == 'tesoura':
    print('Você perdeu!!! Escolhi tesoura.')
elif humano == 'pedra' and jogo == 'papel':
    print('Você perdeu!!! Escolhi papel.')
elif humano == 'papel' and jogo == 'pedra':
    print('Você ganhou!!! Escolhi pedra.')
elif humano == 'tesoura' and jogo == 'pedra':
    print('Você perdeu!!! Escolhi papel.')
elif humano == 'pedra' and jogo == 'tesoura':
    print('Você ganhou!!! Escolhi tesoura.')
elif humano == jogo:
    print('JOKENPÔ! Também escolhi {}'.format(jogo))
else:
    print('BURRO! Escolha pedra, papel ou tesoura.')






