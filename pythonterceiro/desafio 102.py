def fatorial(numero=1, show=False):
    """
    -->Calcula o fatorial mostrando ou não o cálculo.
    :param numero: fatorial a ser calculado
    :param show: lógico opcional, deve ou não mostrar o cálculo
    :return: f
    """
    if show == False:
        f = 1
        for a in range(numero, 0, -1):
            f *= a
        print(f)
    else:
        f = 1
        for a in range(numero, 0, -1):
            f *= a
            if a > 1:
                print(f'{a} x ', end='')
            else:
                print(f'{a} ', end='')
        print(f'! = {f}')


fatorial(5, True)
fatorial(6)
help(fatorial)
