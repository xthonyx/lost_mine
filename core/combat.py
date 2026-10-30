"""
3. Onde fica:

Função, em core/modifiers.py: recebe o valor do atributo e devolve o modificador. Como é regra por faixas, use if/elif ou uma lista de limites. É função e não tabela solta porque a regra pode mudar num lugar só.

A fórmula do dano (rolar os dados da arma + modificador) fica em core/combat.py, juntando dice.py e modifiers.py.

O caminho do dado até o dano, em ordem:

Pega a arma equipada no dicionário de itens.
Lê o campo que diz qual atributo ela usa (é um texto, tipo 'forca').
Usa esse texto como chave no dicionário do personagem pra obter o valor do atributo. Por isso os nomes têm que ser idênticos nos dois lugares.
Passa o valor pela função do modificador.
Rola os dados e soma.

"""