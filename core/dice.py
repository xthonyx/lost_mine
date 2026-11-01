from random import randint

def rolar_dados(qtd_lados=20, qtd_dados=1):
    """
    Função padrão para rolar qualquer combinação de dados. Por padrão
    rola 1d20, como parametro usamos a quantidade de lados e depois
    a quantidade de dados. O retorno da funcao armazena os resultados
    numa lista para fazer uso das rolagens individuais.
    """
    rolagens = []
    for _ in range(qtd_dados):
        resultado = randint(1, qtd_lados)
        rolagens.append(resultado)
    return rolagens