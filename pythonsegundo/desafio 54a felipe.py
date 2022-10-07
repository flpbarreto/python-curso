from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8, 1):
    idade = atual - (int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa))))
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores e {} são menores.'.format(maior, menor))
