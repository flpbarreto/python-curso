def escreva(txt):
    qtde = len(txt)
    a = qtde * 3
    print(f'{"=" * a}\n'
          f'{" " * int(qtde):<}{txt:^}\n'
          f'{"=" * a}')


escreva('Olá mundo')
escreva('cvc')
escreva("Curso de Python no Youtube")
