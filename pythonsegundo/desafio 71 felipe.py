print('-' * 30)
print('{:^30}'.format('BANCO DO FELIPE'))
print('-' * 30, end = '\n')
valor = int(input('Digite o valor a ser sacado R$'))
ced = 50
totalced = 0
while True:
    if totalced > 0 and valor < ced:
        print(f'Serão {totalced} cédulas de {ced}')
    if valor >= ced:
        valor -= ced
        totalced += 1
        #print(valor)
    elif valor >= 20:
        ced = 20
        totalced = 0
    elif valor >= 10:
        ced = 10
        totalced = 0
    elif valor >= 1:
        ced = 1
        totalced = 0
    elif valor == 0:
        break
print('\n---FIM!---')