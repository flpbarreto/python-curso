import random
resposta = random.randint(0, 10)
tentativas = 0
escolha = int
while resposta != escolha:
    escolha = int(input('Digite um número de 0 a 10: '))
    tentativas += 1
print('Você acertou, era número {}. Foram necessárias {} tentativas!'.format(resposta, tentativas))
