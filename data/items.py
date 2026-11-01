ARMAS = {
    'espada_curta': {
        'nome': 'Espada Curta',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
        'tipo': 'armas',
    },

    'espada_longa': {
        'nome': 'Espada Longa',
        'qtd_dados': 1,
        'qtd_lados': 8,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
        'tipo': 'armas',
    },

    'adaga': {
        'nome': 'Adaga',
        'qtd_dados': 1,
        'qtd_lados': 4,
        'atributo': 'destreza',
        'alcance': 'corpo_a_corpo',
        'tipo': 'armas',
    },

    'maca': {
        'nome': 'Maça',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
        'tipo': 'armas',
    },

    'lanca': {
        'nome': 'Lança',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
        'tipo': 'armas',
    },

    'arco_curto': {
        'nome': 'Arco Curto',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'destreza',
        'alcance': 'distancia',
        'tipo': 'armas',
    },

    'desarmado': {
        'nome': 'Desarmado',
        'qtd_dados': 1,
        'qtd_lados': 4,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
        'tipo': 'armas',
    },

}

ARMADURAS = {
    'armadura_couro': {
        'nome': 'Armadura de Couro',
        'ca_base': 11,
        'tipo': 'armaduras',
    },

    'camisao_malha': {
        'nome': 'Camisão de Malha',
        'ca_base': 13,
        'tipo': 'armaduras',
    },

    'cota_malha': {
        'nome': 'Cota de Malha',
        'ca_base': 16,
        'tipo': 'armaduras',
        'exigencia': {
            'forca': 13,
        },
    },

}

ESCUDOS = {
    'escudo': {
        'nome': 'Escudo',
        'ca_bonus': 2,
        'tipo': 'escudos',
        },

}

POCOES = {
    'pocao_pequena': {
        'nome': 'Poção Pequena',
        'qtd_dados': 2,
        'qtd_lados': 6,
        'recuperacao': 'vida',
        'tipo': 'pocoes',
    },

    'pocao_maior': {
        'nome': 'Poção Maior',
        'qtd_dados': 4,
        'qtd_lados': 6,
        'recuperacao': 'vida',
        'tipo': 'pocoes',
    },
}

ITENS = ARMAS | ARMADURAS | ESCUDOS | POCOES
"""
Criado uma variavel contendo todos os dicionarios
para podermos filtrar mais facilmente os TIPOS DE ITENS,
armas, armaduras, pocoes etc. Mas mantendo os dicionarios
originais para organização e criação de mais itens no futuro.
"""