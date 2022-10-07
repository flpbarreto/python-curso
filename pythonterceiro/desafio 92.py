import datetime

data = datetime.datetime.now()
ano = data.year
cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['nascimento'] = int(input('Ano de nascimento [AAAA]: '))
cadastro['carteira'] = int(input('Nº da carteira de trabalho [0 para carteira inexistente]: '))
if cadastro['carteira'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Valor do salário R$'))
    idade = int(ano - cadastro['nascimento'])
    aposentadoria = int(idade + 35)
    print(f'{cadastro["nome"]}\n'
          f'{idade} anos\n'
          f'CTPS: {cadastro["carteira"]}\n'
          f'Ano de contratação: {cadastro["contratacao"]}\n'
          f'Salário: R${cadastro["salario"]:.2f}\n'
          f'Irá se aposentar com {aposentadoria} anos.')
else:
    print(f'{cadastro["nome"]} nasceu em {cadastro["nascimento"]} e não possui carteira de trabalho.')
