km = float(input('digite a quantidade de km: '))
if km <= 200.0:
    valor = 0.50 * km
    print('valor da viagem R${:.2f}'.format(valor))
else:
    valor = 0.45 * km
    print('o valor da viagem é R${:.2f}'.format(valor))
