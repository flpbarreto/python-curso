primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = 0
a = 0
while termos < 10:
    termo = primeiro + (a * razao)
    a += 1
    termos += 1
    print('{}º termo: {}'.format(termos, termo))
extra = int(input('''Deseja mostrar mais quantos termos? 
Para encerrar digite 0.
'''))
termos += 1
while extra != 0:
    while extra > 0:
        termo = primeiro + (a * razao)
        print('{}º termo: {}'.format(termos, termo))
        a += 1
        termos += 1
        extra -= 1
    extra = int(input('''Deseja mostrar mais quantos termos? 
    Para encerrar digite 0.
    '''))
print('---FIM!---')