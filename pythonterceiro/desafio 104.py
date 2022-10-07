def leiaInt(enunciado):
    numero = str(input(enunciado))
    while True:
        if numero.isnumeric():
            return numero
        else:
            numero = str(input(enunciado))


n = leiaInt('Digite um numero inteiro: ')
print(n)