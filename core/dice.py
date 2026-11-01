""""
Foi claro. A divisão que eu faria:

dice.py só rola dados, não conhece regras do jogo.

Uma função rola um dado de N lados. A outra rola vários e soma.
Ela não sabe o que é arma, percepção ou ataque. Só recebe números e devolve números.
Um “d20” não precisa de função própria: é rolar um dado de 20 lados. Uma função a mais só duplicaria a regra.
"""
from random import randint

def rolar_dados(qtd_lados=20, qtd_dados=1):
    rolagens = []
    for _ in range(qtd_dados):
        resultado = randint(1, qtd_lados)
        soma.append(rolagens)
    return soma

    #EM TRABALHO COM CLAUDE