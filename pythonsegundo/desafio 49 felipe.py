n = int(input('digite qual tabuada quer saber: '))
for tab in range (0, 11, 1):
    tabuada = n * tab
    print('{} x {} = {}'.format(tab, n, tabuada))
