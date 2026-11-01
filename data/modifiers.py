def calcular_proficiencia(valor_atributo):
    """
    Recebe um valor numerico referente a um atributo do personagem
    (forca, inteligencia, destreza, etc) e faz o calculo de quanto
    de bonus vai receber, indo de 8 a 20, e recebendo um bonus de -1 a +5.
    Range: 8-9 = -1 ; 10-11 = +0 ; 12-13 = +1 ; 14-15 = +2 ;
    16-17 = +3 ; 18-19 = +4; 20 = +5
    """
    bonus_proficiencia = (valor_atributo - 10) // 2
    return bonus_proficiencia