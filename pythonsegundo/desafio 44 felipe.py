preco = float(input('digite o preço do produto: R$'))
pag = int(input('Digite 1 pagamento à vista com dinheiro ou cheque\n2 para pagamento à vista no cartão de crédito\n3 para pagamento em até 2x no cartão de crédito\n4 para pagamento em 3x ou mais no cartao de crédito\n'))
if pag == 1:
    valor = preco - (preco / 10)
elif pag == 2:
    valor = preco - ((preco / 100) * 5)
elif pag == 3:
    valor = preco
elif pag == 4:
    valor = preco + (preco / 5)
else:
    print('ERRO!!!')
print('o valor a ser pago é R${:.2f}'.format(valor))
