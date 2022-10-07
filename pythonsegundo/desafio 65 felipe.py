num = 0
continuar = ''
med = 0
maior = 0
menor = 0
media = float
cont = 0
while continuar != 'não' and continuar != 'n' and continuar != 'nao':
    num = int(input('\033[1;31mDigite um valor inteiro:\033[m '))
    med += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1
    if cont == 1:
        menor = num
    continuar = input('\033[1;33mDesaja continuar?\033[m ').strip().lower()
media = (med / cont)
print('''a média dos valores é {:.2f}
o maior valor é {}
o menor valor é {}'''.format(media, maior, menor))
