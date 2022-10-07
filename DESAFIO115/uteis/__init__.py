def cadastrar():
    try:
        cadastro = dict()
        while True:
            nome = str(input('Nome: ').strip())
            if nome.isalpha():
                break
        while True:
            idade = str(input('Idade: '))
            if idade.isnumeric():
                idade = float(idade)
                break
        cadastro['nome'] = nome
        cadastro['idade'] = idade
        a = cadastro.copy()
        del cadastro
        return a

    except Exception as erro:
        print(erro)