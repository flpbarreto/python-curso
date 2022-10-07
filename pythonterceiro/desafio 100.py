import random
from time import sleep

def sorteia(lista):
    for a in range(0, 5):
        lista.append(random.randint(1, 100))
        print(lista[a], end=' ')
        sleep(0.5)

def somapar(lista):
    soma = 0
    print('\nA soma dos pares é:', end=' ')
    for a in range(0, len(lista)):
        if (lista[a] % 2) == 0:
            soma += lista[a]
    print(f'{soma}')


numeros = list()


sorteia(numeros)

somapar(numeros)

