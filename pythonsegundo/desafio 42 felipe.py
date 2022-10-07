l1 = float(input('digite o valor do primeiro lado: '))
l2 = float(input("digite o valor do segundo lado: "))
l3 = float(input('digite o valor do terceiro lado: '))
if l3 > l2 and l3 > l1:
    if (l2 + l1) > l3:
        if l3 == l2 and l2 == l1 and l1 == l3:
            print('o triângulo existe e é equilátero')
        elif l3 == l2 or l2 == l1 or l1 == l3:
            print('o triângulo existe e é isósceles')
        else:
            print('o triângulo existe e é escaleno')
    else:
        print('o triangulo não existe')
elif l2 > l3 and l2 > l1:
    if (l3 + l1) > l2:
        if l3 == l2 and l2 == l1 and l1 == l3:
            print('o triângulo existe e é equilátero')
        elif l3 == l2 or l2 == l1 or l1 == l3:
            print('o triângulo existe e é isósceles')
        else:
            print('o triângulo existe e é escaleno')
    else:
        print('o triangulo não existe')
elif l1 > l2 and l1 > l3:
    if (l2 + l3) > l1:
        if l3 == l2 and l2 == l1 and l1 == l3:
            print('o triângulo existe e é equilátero')
        elif l3 == l2 or l2 == l1 or l1 == l3:
            print('o triângulo existe e é isósceles')
        else:
            print('o triângulo existe e é escaleno')
    else:
        print('o triangulo não existe!')
