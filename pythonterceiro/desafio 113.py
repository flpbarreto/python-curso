def leiaInt(enunciado):
    while True:
        try:
            numero = str(input(enunciado)).strip()

            if numero.isnumeric():
                return numero
        except ValueError:
            print(f'ERRO! Número inválido. Tente novamente!')


def leiaFloat(enunciado):
    while True:
        try:
            numero = str(input(enunciado)).strip().replace(',', '.')
            n = float(numero)
            return n
        except ValueError:
            print(f'ERRO! Valor inválido.Tente novamente!')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um valor')
            return 0




n = leiaInt('Digite um numero inteiro: ')
n1 = leiaFloat('Digite um número real: ')
print(f'O número inteiro é {n} e o real é {n1}')
