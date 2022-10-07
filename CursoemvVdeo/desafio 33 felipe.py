n1 = float(input('digite um número: '))
n2 = float(input('digite um número: '))
n3 = float(input('digite um número: '))
if n3 > n2 > n1:
    print('maior: {} menor: {}'.format(n3, n1))
if n2 > n1 > n3:
    print('maior: {} menor: {}'.format(n2, n3))
if n1 > n3 > n2:
    print('maior: {} menor: {}'.format(n1, n2))
