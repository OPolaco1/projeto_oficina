#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *

FREQUENCIA = 60

LARGURA,ALTURA = 800,800

TELA = criar_tela_base(LARGURA,ALTURA)

IMG_BARRA = carregar_imagem("barra.png" ,80 , 30)


SETA_ESQUERDA = pg.K_LEFT
SETA_DIREITA = pg.K_RIGHT
#LIMITE_ESQUERDO = 0 + IMG_BARRA // 2
#LIMITE_DIREITO = LARGURA - IMG_BARRA // 2




Barra = definir_estrutura("barra","x y dx")

BARRA_INICIAL = Barra(LARGURA // 2 , ALTURA // 2 + LARGURA // 2.5, 0)


def desenha(barra):
    colocar_imagem_sobre_tela_e_mostrar(IMG_BARRA , barra.x , barra.y)


def mover_barra(barra):
    posicao = barra.x + barra.dx
    return barra(posicao, barra.dx)


def trata_tecla(barra,tecla):
    if tecla == SETA_ESQUERDA:
        return barra.dx - 3
    elif tecla == SETA_DIREITA:
        return barra.dx + 3
    #else
    return barra



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

