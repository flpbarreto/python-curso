frase = input('digite uma frase: ')
frase = frase.strip()
a = frase.count('A')
b = frase.count('a')
c = a+b
d = frase.find('a')
e = frase.rfind('a')
print('"a" aparece {} vezes. a primeira está na posição {} e a ultima na {}'.format(c, d, e))
