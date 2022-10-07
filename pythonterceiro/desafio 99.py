def maior(* lista):
    for a in range(0, len(lista)):
        if a == 0:
            m = lista[a]
        if lista[a] > m:
            m = lista[a]
    print(f'O maior valor é {m}')


maior(1, 5, 9)
maior(10, 3, 56, 12)
maior(89, 2)