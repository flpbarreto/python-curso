valorcasa = float(input('digite o valor da casa: '))
salario = float(input('digite o valor do seu salário: '))
prazo = float(input('digite o prazo, em anos, no qual deseja quitar o empréstimo: '))
prazo = prazo * 12
mensalidade = (valorcasa / prazo)
if mensalidade > ((salario / 10) * 3):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO APROVADO!')
    print('Valor do imóvel: {:.2f}'.format(valorcasa))
    print('Valor da prestação: {:.2f}'.format(mensalidade))
    print('Prazo para quitação do empréstimo: {:.1f} anos'.format(prazo/12))
