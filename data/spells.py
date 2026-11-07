MAGIAS = {
    'magia_teste': {
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
    },
    'chama_sagrada': {
        'nome': 'Chama Sagrada',
        'nivel': 0,
        'efeito': 'dano',
        'qtd_dados': 1,
        'qtd_lados': 8,
        'atributo': 'sabedoria',
        'alvo': 'inimigo',
    },
    'orientacao': {
        'nome': 'Orientação',
        'nivel': 0,
        'efeito': 'buff',
        'atributo': 'sabedoria',
        'alvo': 'aliado',
        'modifica': 'testes',
        'duracao': 1,
        'bonus_qtd_dados': 1,
        'bonus_qtd_lados': 4,
    },
    'palavra_de_cura': {
        'nome': 'Palavra de Cura',
        'nivel': 1,
        'efeito': 'cura',
        'qtd_dados': 1,
        'qtd_lados': 4,
        'atributo': 'sabedoria',
        'alvo': 'aliado',
        'recuperacao': 'vida',
    },
    'infligir_ferimentos': {
        'nome': 'Infligir Ferimentos',
        'nivel': 1,
        'efeito': 'dano',
        'qtd_dados': 3,
        'qtd_lados': 10,
        'atributo': 'sabedoria',
        'alvo': 'inimigo',
    },
    'raio_de_fogo': {
        'nome': 'Raio de Fogo',
        'nivel': 0,
        'efeito': 'dano',
        'qtd_dados': 1,
        'qtd_lados': 10,
        'atributo': 'inteligencia',
        'alvo': 'inimigo',
    },
    'armadura_de_mago': {
        'nome': 'Armadura de Mago',
        'nivel': 1,
        'efeito': 'buff',
        'atributo': 'inteligencia',
        'alvo': 'aliado',
        'modifica': 'ca_base',
        'valor': 13,
        'duracao': {
            'horas': 8
        },
    },
    'misseis_magicos': {
        'nome': 'Mísseis Mágicos',
        'nivel': 1,
        'efeito': 'dano',
        'qtd_dados': 1,
        'qtd_lados': 4,
        'alvo': 'inimigo',
        'bonus': 1,
        'repeticoes': 3,
        'acerto': 'automatico',
    },
}