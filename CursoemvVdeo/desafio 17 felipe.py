from math import sqrt
n1 = float(input('digite o valor do cateto adjacente: '))
n2 = float(input('digite o valor do cateto oposto: '))
h = sqrt((n1**2)+(n2**2))
print('o valor da hipotenusa é {:.2f}'.format(h))
