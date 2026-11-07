# from data.items import ITENS
# from data.classes import CLASSES
# from data.enemies import INIMIGOS

# SLOTS = {'arma': 'armas', 'armadura': 'armaduras', 'escudo': 'escudos'}


# def conferir(grupo, nome_grupo):
#     for nome, dados in grupo.items():
#         for item in dados['inventario']:
#             if item not in ITENS:
#                 print(f"{nome_grupo} {nome}: '{item}' do inventario nao existe")

#         if 'equipamento' not in dados:
#             print(f"{nome_grupo} {nome}: falta o bloco 'equipamento'")
#             continue

#         for slot, item in dados['equipamento'].items():
#             if item is None:
#                 continue
#             if item not in ITENS:
#                 print(f"{nome_grupo} {nome}: '{item}' do equipamento nao existe")
#             elif ITENS[item]['tipo'] != SLOTS[slot]:
#                 print(f"{nome_grupo} {nome}: '{item}' nao serve pro slot '{slot}'")


# conferir(CLASSES, 'Classe')
# conferir(INIMIGOS, 'Inimigo')
# print('Conferencia terminada.')

# from data.modifiers import calcular_proficiencia


# def vida_inicial(dado_vida, constituicao):
#     proficiencia = calcular_proficiencia(constituicao)
#     vida = dado_vida + proficiencia
#     return vida
# print(vida_inicial(10, 14))   # 12
# print(vida_inicial(6, 13))    # 7
# print(vida_inicial(8, 14)) 

from core.characters import criar_personagem
from data.classes import CLASSES

personagem = criar_personagem('Anthony', CLASSES['mago'])

print(personagem)

personagem['inventario']['pocao_maior'] -= 1

print(personagem['inventario'])
print(CLASSES['mago']['inventario'])