#CRIAR DICIONARIOS PARA CADA TIPO DE ITEM, ARMA, ESCUDO, ARMADURA, POCOES, CHAVES, TESOUROS, DINHEIRO/GOLD?


ARMAS = {
    'espada_curta': {
        'nome': 'Espada curta',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
    },

    'espada_longa': {
        'nome': 'Espada Longa',
        'qtd_dados': 1,
        'qtd_lados': 8,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
    },

    'adaga': {
        'nome': 'Adaga',
        'qtd_dados': 1,
        'qtd_lados': 4,
        'atributo': 'destreza',
        'alcance': 'corpo_a_corpo',
    },

    'maca': {
        'nome': 'Maça',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
    },

    'lanca': {
        'nome': 'Lança',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
    },   

    'arco_curto': {
        'nome': 'Arco curto',
        'qtd_dados': 1,
        'qtd_lados': 6,
        'atributo': 'destreza',
        'alcance': 'distancia',
    },

    'desarmado': {
        'nome': 'Desarmado',
        'qtd_dados': 1,
        'qtd_lados': 4,
        'atributo': 'forca',
        'alcance': 'corpo_a_corpo',
    },

}

ARMADURAS = {
    'armadura_couro': {
        'ca_base': 11,
    },

    'camisao_malha': {
        'ca_base': 13,
    },

    'cota_malha': {
        'ca_base': 16,
        'exigencia': {
            'forca': 13,
        },

    },

}

ESCUDOS = {
    'escudo': {
        'ca_bonus': 2
        }

    }