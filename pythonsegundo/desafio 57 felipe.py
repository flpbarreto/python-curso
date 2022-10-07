sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = input('Digite M para masculino e F para feminino: ').strip()
if sexo == 'm':
    print('O sexo é masculino!')
else:
    print('O sexo é feminino!')
