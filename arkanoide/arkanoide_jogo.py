#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *

FREQUENCIA = 60

LARGURA,ALTURA = 800,800

TELA = criar_tela_base(LARGURA,ALTURA)

IMG_BARRA = carregar_imagem("barra.png" ,80 , 30)



SETA_ESQUERDA = pg.K_a
SETA_DIREITA = pg.K_d
LIMITE_ESQUERDO = 0 + largura_imagem(IMG_BARRA) // 4
LIMITE_DIREITO = LARGURA - largura_imagem(IMG_BARRA) // 4




Barra = definir_estrutura("barra","x y ")
Y = ALTURA // 2 + LARGURA // 2.5
BARRA_INICIAL = Barra(LARGURA // 2 , Y)




def desenha(barra):
    if (barra.x < LIMITE_DIREITO and barra.x > LIMITE_ESQUERDO):
        colocar_imagem(IMG_BARRA,TELA,barra.x,Y)
    elif (barra.x <= LIMITE_DIREITO):
        colocar_imagem(IMG_BARRA,TELA,LIMITE_ESQUERDO,Y)
    elif (barra.x >= LIMITE_ESQUERDO):
        colocar_imagem(IMG_BARRA,TELA,LIMITE_DIREITO,Y)




def trata_tecla(barra,tecla):
    if tecla == SETA_ESQUERDA:
        return Barra(barra.x - 3, Y)
    elif tecla == SETA_DIREITA:
        return Barra(barra.x + 3, Y)
    #else
    return barra


def mover_barra(barra):

    posicao = barra.x
    return Barra(posicao, Y,)





#print(BARRA_INICIAL)
'''


Barra pode ser formada por: Int[

'''

'''
retan = IMG_BARRA


def desenhar(retan):
    return colocar_imagem_sobre_tela_e_mostrar(retan,400,700)



desenhar(retan)
'''

