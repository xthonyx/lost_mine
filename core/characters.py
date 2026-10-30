# arquivo direcionado para colocar todas as informações dos heróis.
'''
Nome via input
Classe : Guerreiro, Mago, Ladino, Clérigo.

Vida e constituicao = classes frageis usam d6(media de 4 pontos); classes agéis/suporte usam d8(media de 5); classes de frente usam d10(media 6 pontos) // isso mais o modificador de constituição

vida = modificador de constituição + rolagem de dado da classe(ou media do dado)(usar rolagem de dado pode trazer variação na gameplay)

Tabela dos modificadores ((valor do atributo - 10) / 2)) arredondado para baixo.

8-9 = -1 ; 10-11 = +0 ; 12-13 = +1 ; 14-15 = +2 ; 16-17 = +3; 18-19 = +4; 20 = +5

CA = CA da armadura + modificador de destreza 









'''

'''3. A função da CA (core/characters.py)
 Recebe o personagem e o dicionário de itens, e devolve um número.
Parte de uma CA base (sem nada equipado; você define o valor).
Soma: bônus da armadura se houver + modificador de destreza (usando a função do modifiers) + bônus do escudo se houver.
Cada “se houver” é uma verificação de None.
Receber o dicionário de itens como parâmetro, em vez de importá-lo, mantém o motor independente do conteúdo. '''