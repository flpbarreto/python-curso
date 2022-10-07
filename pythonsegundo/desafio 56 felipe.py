nome = ''
idhomem = 0
abaixovinte = 0
med = 0
for pessoa in range (1, 5, 1):
    print('----{}ª pessoa----'.format(pessoa))
    nome = input('Digite seu nome: ').strip().lower()
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Digite 1 para masculino ou 2 para feminino: '))
    med += idade
    if pessoa == 1 and sexo == 1:
        homem = nome
        idhomem = idade
    else:
        if sexo == 2 and idade < 20:
            abaixovinte += 1
        if sexo == 1 and idade > idhomem:
            homem = nome
            idhomem = idade
media = (med / 4)
print('''O homem mais velho é {};
{} mulheres têm menos de 20 anos;
a média das idades é {}.'''.format(homem, abaixovinte, media))
