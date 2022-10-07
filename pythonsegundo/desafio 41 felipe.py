ano = int(input('digite o ano do seu nascimento: '))
categoria = 2021 - ano
if categoria <= 9:
    print('categoria: MIRIM')
elif categoria <= 14 and categoria > 9:
    print('categoria: INFANTIL')
elif categoria <= 19 and categoria > 14:
    print('categoria: JUNIOR')
elif categoria <= 20 and categoria > 19:
    print('categoria: SÊNIOR')
else:
    print('categoria: MASTER')
