def area(l, c):
    a = c * l
    print(f'A área do terreno é {a:.2f}m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)