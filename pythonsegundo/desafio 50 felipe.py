a = int(input('digite um numero inteiro: '))
b = int(input('digite um numero inteiro: '))
c = int(input('digite um numero inteiro: '))
d = int(input('digite um numero inteiro: '))
e = int(input('digite um numero inteiro: '))
f = int(input('digite um numero inteiro: '))
lista = [a, b, c, d, e, f]
soma = 0
for x in range (0, 6, 1):
    if (lista[x]) % 2 == 0:
        soma = soma + lista[x]
print('a soma dos numeros pares é {}'.format(soma))
