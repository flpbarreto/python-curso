def voto(ano):
    """
    Retorna se um indivíduo tem voto obrigatório, opcional ou não vota com base no ano de nascimento.
    :param ano: ano de nascimento.
    :return: sem retorno.
    """
    import datetime

    atual = datetime.date.today().year
    idade = atual - ano
    if 16 <= idade  < 18 or idade >= 60:
        print('VOTO OPCIONAL')
    if idade < 16:
        print('NÃO VOTA')
    if 18 <= idade < 60:
            print('VOTO OBRIGATÓRIO')


a = int(input('Digite o ano de nascimento: '))
voto(a)
