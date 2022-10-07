decimal = int(input('digite um numero inteiro: '))
base = int(input('''Digite 
[ 1 ] para binário
[ 2 ] para octal ou
[ 3 ] para hexadecimal
Opção: '''))
if base == 1:
    print('decimal: {}. binário: {}'.format(decimal, bin(decimal)[2:]))
elif base == 2:
    print('decimal: {}. octal: {}'.format(decimal, oct(decimal)[2:]))
elif base == 3:
    print('decimal: {}. hexadecimal: {}'.format(decimal, hex(decimal)[2:]))
else:
    print('Opção inválida!')
