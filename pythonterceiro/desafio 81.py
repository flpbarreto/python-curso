lista = list()
cont = str
num = int
while cont != 'n':
    num = input('Digite um valor inteiro: ')
    lista.append(num)
    cont = str(input('Deseja continuar [S/N]? ').lower())

print(f'foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(lista)
if '5' in lista:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
