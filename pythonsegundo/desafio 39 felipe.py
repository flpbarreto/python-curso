idade = int(input('digite sua idade: '))
if idade == 18:
    print('está na hora de se alistar!')
elif idade > 18:
    print('já passou da hora de se alistar, você está {} anos atrasado!'.format(idade - 18))
else:
    print('ainda não é hora de se alistar, faltam {} anos para se alistar!'.format(18 - idade))
