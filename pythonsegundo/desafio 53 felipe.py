frase = input('Digite uma frase: ').strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('''{} é igual a {}
    É um palíndromo!'''.format(junto, inverso))
else:
    print('''{} não é igual a {}
    Pontanto não é um palíndromo!'''.format(junto, inverso))
