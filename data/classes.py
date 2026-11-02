"""
Arquivo contendo apenas os DADOS das classes, atributos e inventário.

"""

CLASSES = {

   

    'guerreiro': {
        'nome': 'Guerreiro',
        'atributos': {
            'constituicao': 14,
            'destreza': 13,
            'forca': 15,
            'inteligencia': 10,
            'sabedoria': 12,
            'carisma': 8,
        },
        'inventario': {
            'espada_curta': 1,
            'arco_curto': 1,
            'pocao_pequena': 3,
        },
        'equipamento': {
            'arma':'espada_longa',
            'armadura': 'cota_malha',
            'escudo': 'escudo',
        },
        'dado_vida': 10,

    },

    'mago': {
        'nome': 'Mago',
        'atributos': {
            'constituicao': 13,
            'destreza': 14,
            'forca': 8,
            'inteligencia': 15,
            'sabedoria': 12,
            'carisma': 10,
        },
        'inventario': {
            'arco_curto': 1,
            'pocao_maior': 3,
        },
        'equipamento': {
            'arma':'adaga',
            'armadura': 'armadura_couro',
            'escudo': None,
        },
        'dado_vida': 6,
    },

    'ladino': {
        'nome': 'Ladino',
        'atributos': {
            'constituicao': 14,
            'destreza': 15,
            'forca': 8,
            'inteligencia': 10,
            'sabedoria': 12,
            'carisma':10,
        },
        'inventario': {
            'rapieira': 1,
            'arco_curto': 1,
            'pocao_pequena': 2,
        },
        'equipamento': {
            'arma':'adaga',
            'armadura': 'armadura_couro',
            'escudo': None,
        },
        'dado_vida': 8,
    },

    'clerigo': {
        'nome': 'Clérigo',
        'atributos': {
            'constituicao': 14,
            'destreza': 12,
            'forca': 13,
            'inteligencia': 8,
            'sabedoria': 15,
            'carisma': 10,
        },
        'inventario': {
            'pocao_maior': 5,
        },
        'equipamento': {
            'arma': 'maca',
            'armadura': 'cota_malha',
            'escudo': 'escudo',
        },
        'dado_vida': 8,

    },
}