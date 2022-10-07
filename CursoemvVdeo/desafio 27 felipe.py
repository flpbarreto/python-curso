nome = input('digite seu nome completo: ').strip()
lista = nome.split()
ultimo = len(lista) - 1
print('primeiro {}. ultimo: {}'.format(lista[0], lista[ultimo]))
