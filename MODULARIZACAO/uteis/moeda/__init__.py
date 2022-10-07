def dobro(n, f=True):
    if f == False:
        return (n * 2)
    else:
        return 'R$''{:.2f}'.format(n * 2)

def metade(n, f=True):
    if f == False:
        return (n / 2)
    else:
        return 'R$''{:.2f}'.format(n / 2)

def aumentar(n, p, f=True):
    if f == False:
        return n + (n * (p / 100))
    else:
        return 'R$''{:.2f}'.format(n + (n * (p / 100)))

def diminuir(n, p, f=True):
    if f == True:
        res = float(n - (n * (p / 100)))
        return 'R$''{:.2f}'.format(res)
    else:
        res = float(n - (n * (p / 100)))
        return res

def moeda(n):
    return 'R$''{:.2f}'.format(n)

def resumo(n, m=0, d=0):
    print('=' * 25)
    print('      RESUMO DO DIA')
    print('=' * 25)
    print(f'Preço analisado: {moeda(n)}\n'
          f'Dobro do preço: {dobro(n)}\n'
          f'Metdade do preço: {metade(n)}\n'
          f'{m}% de aumento: {aumentar(n, m)}\n'
          f'{d}% de redução: {diminuir(n, d)}')
    print('-' * 25)


def entrada(msg):
    num = str(input(msg)).replace(',', '.').strip()
    while True:
        if num == '' or num.isalnum():
            print(f'{num} é inválido, digite um valor válido:', end=' R$')
            num = str(input()).replace(',', '.').strip()
        else:
            return float(num)
