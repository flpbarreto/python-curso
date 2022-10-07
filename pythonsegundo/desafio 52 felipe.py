num = int(input('Digite um número: '))
controle = 0
for x in range (1, num + 1, 1):
    if (num % x) == 0:
        print('\033[1;31m{}\033[m'.format(x))
        controle += 1
    else:
        print('\033[0;33m{}\033[m'.format(x))
if controle > 2:
    print('{} não é primo'.format(num))
else:
    print('{} é primo'.format(num))

