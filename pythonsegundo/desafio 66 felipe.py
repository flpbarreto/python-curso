soma = 0
n = 0
cont = 0
while n != 999:
    n = int(input('''Digite um número:
    Para sair digite 999
    '''))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos números é {soma} e foram digitados {cont} números.')
