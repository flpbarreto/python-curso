import math
n = float(input('digite o valor do angulo: '))
s = math.sin(n)
c = math.cos(n)
t = math.tan(n)
print('angulo: {}, sen: {:.2f}, cos: {:.2f}, tg: {:.2f}'.format(n, s, c, t))
