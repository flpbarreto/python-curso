print('=' * 30, end=' ')
print('LOJA DO FELIPE', end=' ')
print('=' * 30, end='\n')
valor = float(input('Valor a ser pago: '))
forma = int(input('''[ 1 ] À vista\n
[ 2 ] À vista no cartão\n
[ 3 ] Até 2x no cartão\n
[ 4 ] 3x ou mais no cartão\n
Forma de pagamento: '''))
while forma >= 5 or forma < 1:
    forma = int(input('Forma de pagamento: '))
valorfinal = float
if forma == 1:
    valorfinal = float(valor - (valor / 10))
elif forma == 2:
    valorfinal = float(valor - (valor / 20))
if forma == 3:
    valorfinal = float(valor)
if forma == 4:
    valorfinal = float(valor + ((valor / 10) * 2))


print(f'O valor a ser pago é R${valorfinal:.2f}.')