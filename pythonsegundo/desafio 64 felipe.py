cont = 0
num = 0
soma = 0
while num != 999:
    num = int(input('''Digite um número
    Para sair digite 999
    '''))
    if num != 999:
        soma += num
        cont += 1
print('A soma dos números é {}, foram digitados {} números'.format(soma, cont))
