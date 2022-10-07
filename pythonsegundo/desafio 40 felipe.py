n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7.0:
    print('APROVADO! NOTA: {:.1f}'.format(media))
elif 6.9 >= media and media >= 5.0:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO! NOTA: {:.1f}'.format(media))
else:
    print('REPROVADO! NOTA: {:.1f}'.format(media))
