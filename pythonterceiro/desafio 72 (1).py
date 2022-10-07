d = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
b = int(input('Digite um número entre 0 e 20: '))
a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
     'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while (b > 20) or (b < 0):
    b = b = int(input('ERRO!\nDigite um número entre 0 e 20: '))
c = d.index(b)
print(f'Você digitou {a[c]}.')