lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O valor {n} foi adicionado à última posição')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O valor {n} foi adicionado na posição {pos}')
                break
            pos += 1
print(lista)
