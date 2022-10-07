#DOCSTRINGS:
#from time import sleep

#def contador(i, f, p):
#    """
#    Faz uma contagem de i até f com passo igual a p.
#    :param i: número de início da contagem.
#    :param f: número final da contagem.
#    :param p: passo da contagem.
#    :return: sem retorno.
#    """
#    while p == 0:
#        p = int(input(f'ERRO!\n'
#              f'O Valor do passo não pode ser 0.\n'
#              f'Digite outro valor: '))

#    if p < 0:
#        p *= -1

#    if i < f:
#        while True:
#            print(i, end=' ')
#            if (i + p) > f:
#                break
#            i += p
#            sleep(0.5)

#    if i > f:
#        while True:
#            print(i, end=' ')
#            if i < (f + p):
#                break
#            i -= p
#            sleep(0.5)


#help(contador)

#FATORIAL COM USO DO RETURN:

#def fatorial(numero=1):
#    f = 1
#    for c in range(numero, 1, -1):
#        f *= c
#    return f

#fat = fatorial(5)
#print(f'O fatorial de 5 é {fat}')

import math
help(math)