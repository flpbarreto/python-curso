n = int(input('Digite o número de termos que deseja ver: '))
print('~' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('~' * 30)
t1 = 0
t2 = 1
cont = 0
print('{} -> {} -> '.format(t1, t2), end = '')
while cont <= n:
    t3 = t1 + t2
    if cont != n:
        print('{} -> '.format(t3), end = '')
    else:
        print('{}'.format(t3))
    t1 = t2
    t2 = t3
    cont += 1
print('-' * 30, end = '')
print('FIM!', end = '')
print('-' * 30)
