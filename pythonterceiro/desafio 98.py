from time import sleep

a = int
for a in range(1, 11):
    print(a, end=' ')
    sleep(0.5)

print()
a = 10
while a >= 0:
    print(a, end=' ')
    sleep(0.5)
    a -= 2

def contador(i, f, p):

    while p == 0:
        p = int(input(f'ERRO!\n'
              f'O Valor do passo não pode ser 0.\n'
              f'Digite outro valor: '))

    if p < 0:
        p *= -1

    if i < f:
        while True:
            print(i, end=' ')
            if (i + p) > f:
                break
            i += p
            sleep(0.5)

    if i > f:
        while True:
            print(i, end=' ')
            if i < (f + p):
                break
            i -= p
            sleep(0.5)

print()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)