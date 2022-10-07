vel = float(input('digite a velocidade: '))
if vel > 80.0:
    multa = (vel - 80.0) * 7.0
    print('MULTADO! R${:.2f}'.format(multa))
else:
    print('NÃO MULTADO!')
