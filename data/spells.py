# 'nome'
# 'nivel': 0 não gasta slot, 1 ou mais gasta um slot daquele nível
# 'efeito': 'dano' ou 'cura' ou 'buff' ou 'debuff'
# 'qtd_dados' e 'qtd_lados'
# 'atributo': qual atributo dá o bônus
MAGIAS = {
    'magia_1': {
        'nome': 'nome',
        'nivel': 0,
        'efeito': 'dano',
        'qtd_dados': 1,
        'qtd_lados': 4,
        'atributo': 'inteligencia',
        'alvo': 'inimigo', #si ou aliado
        'modifica': 'ca_base', #Qual alteracao a magia vai fazer
        'bonus': 10, #positivo para buff ou negativo para debuff
        'duracao': 1, #quantos turnos dura o efeito
        'bonus_qtd_dados': 1, #bonus de rolagem
        'bonus_qtd_lados': 1, #bonus de rolagem

    }
}

#CHAT GEMINI COM ALGUMAS MAGIAS, SELECIONAR SO ALGUMAS APENAS PARA MAGO E CLERIGO