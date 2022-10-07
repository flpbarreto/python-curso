primeiro = int(input('digite o primeiro termo: '))
progressao = int(input('digite a progressão: '))
for x in range (0, 10, 1):
    print('{}'.format(primeiro))
    primeiro = primeiro +progressao
