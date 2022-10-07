nome = input('digite seu nome: ')
n = nome.upper()
n = n
if n == 'FELIPE':
    print('prazer, felipe')
else:
    print('bom dia {}'.format(nome))
print('prazer, felipe' if n == 'FELIPE' else 'bom dia {}'.format(nome))