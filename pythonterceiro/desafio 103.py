def cadastro(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0

    #gols = int(input('Quantidade de gols: '))
    print(f'O jogador {nome} fez {gols} gols!')



n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))

cadastro(n, g)