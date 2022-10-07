a = int(input('Digite o ano de seu nascimento: '))
b = int(input('Digite o ano de seu nascimento: '))
c = int(input('Digite o ano de seu nascimento: '))
d = int(input('Digite o ano de seu nascimento: '))
e = int(input('Digite o ano de seu nascimento: '))
f = int(input('Digite o ano de seu nascimento: '))
g = int(input('Digite o ano de seu nascimento: '))
cont = 0
contador = 0
if (2021 - a) >= 18:
    cont = cont + 1
else:
    contador = contador + 1
if (2021 - b) >= 18:
    cont = cont + 1
else:
    contador = contador + 1
if (2021 - c) >= 18:
    cont = cont + 1
else:
    contador = contador + 1
if (2021 - d) >= 18:
    cont = cont + 1
else:
    contador += 1
if (2021 - e) >= 18:
    cont = cont + 1
else:
    contador += 1
if (2021 - f) >= 18:
    cont = cont + 1
else:
    contador += 1
if (2021 - g) >= 18:
    cont = cont + 1
else:
    contador += 1
print('{} tem 18 anos ou mais e {} tem menos de 18 anos'.format(cont, contador))