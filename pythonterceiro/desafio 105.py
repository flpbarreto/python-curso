def notas(* n, sit=False):
    """
    Lê várias notas e retorna indormações com base nos dados.
    :param n: notas dos alunos
    :param sit: False ou True para ver a situação da turma com base na média
    :return: dicionário contendo quantidade de notas lançadas, média, maior nota e situação(opcional) da turma
    """
    soma = 0
    maior = 0
    dic = dict()
    media = 0
    for a in range(0, len(n)):
        if a == 0:
            maior = n[a]
        if n[a] > maior:
            maior = n[a]
        soma += n[a]
    dic['qtde'] = len(n)
    dic['media'] = float((soma) / len(n))
    dic['maior'] = maior
    if sit==True:
        if dic['media'] >= 7.0:
            dic['situacao'] = 'BOA!'
        if 7.0 > dic['media'] >= 4.0:
            dic['situacao'] = 'RAZOÁVEL!'
        if dic['media'] < 4.0:
            dic['situacao'] = 'RUIM!'
    return dic

dicionario = notas(7, 7)
print(dicionario)