aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média: '))

print(f'{aluno["nome"]} está com média {aluno["media"]} e portanto', end=' ')
if aluno['media'] < 7.0:
    print('REPROVADO!')
else:
    print('APROVADO!')
