maior = 0
menor = 0
pessoa = 0
for pessoa in range (1, 6, 1):
    kg = float(input('Digite seu peso em kg: '))
    if pessoa == 1:
        menor = kg
        maior = kg
    else:
        if kg > maior:
            maior = kg
            pesmaior = pessoa
        elif kg < menor:
            menor = kg
            pesmenor = pessoa
print ('''A {} pessoa tem o maior peso, {:.1f}kg.
Já a {} pessoa tem o menor peso, {:.1f}kg.'''.format(pesmaior, maior, pesmenor, menor))
