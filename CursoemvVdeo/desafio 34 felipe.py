salario = float(input('digite o salário: '))
if (salario <= 1250.00):
    aumento = (salario / 100) * 15
    novo = salario + aumento
    print('valor do aumento: {:.2f} \nnovo salario: {:.2f}'.format(aumento, novo))
else:
    aumento = salario / 10
    novo = salario + aumento
    print('valor do aumento: {:.2f} \nnovo salario: {:.2f}'.format(aumento, novo))
