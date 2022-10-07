ano = int(input('digite o ano: '))
if (ano % 4) == 0:
    print('{} é ano bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))
