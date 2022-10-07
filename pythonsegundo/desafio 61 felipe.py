primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = 0
a = 0
while termos < 10:
    termo = primeiro + (a * razao)
    a += 1
    termos += 1
    print('{}º termo: {}'.format(termos, termo))
