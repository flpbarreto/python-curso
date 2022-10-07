op = 0
while op != 1 and op != 2 and op != 3 or op == 4 and op != 5:
    a = float(input('Digite um valor: '))
    b = float(input('Digite outro valor: '))
    op = int(input('''Digite
    [ 1 ] para somar
    [ 2 ] para multiplicar
    [ 3 ] para verificar qual o maior valor
    [ 4 ] para digitar novos valores
    [ 5 ] para sair do programa
    '''))
    if op == 1:
        resultado = a + b
    elif op == 2:
        resultado = a * b
    elif op == 3:
        if a > b:
            resultado = a
        elif a == b:
            resultado = str('{} = {}'.format(a, b))
        else:
            resultado = b
    elif op == 5:
        resultado = str('---FIM!---')
        break
print(resultado)