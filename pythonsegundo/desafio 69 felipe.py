sexo = ''
idade = 0
continuar = ''
maiores = 0
homens = 0
mulheres = 0
while continuar != 'n':
    print('-' * 20)
    print('\033[7mCADASTRE UMA PESSOA\033[m')
    print('-' * 20)
    while sexo != 'm' and sexo != 'f':
        sexo = input('\033[1;31mMasculino ou Feminino [M/F]?\033[m ').strip().lower()
    idade = int(input('\033[1;33mDigite a idade:\033[m '))
    if idade >= 18:
        maiores += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    while continuar != 'n' and continuar != 's':
        continuar = str(input('\033[1;46mDeseja continuar [S/N]?\033[m ')).strip().lower()
    sexo = ''
    if continuar == 'n':
        break
    continuar = ''
print('\nRESULTADOS:')
print(f'{maiores} pessoas têm mais de 18 anos, {homens} homens foram cadastrados e {mulheres} mulheres têm menos de 20 anos.')