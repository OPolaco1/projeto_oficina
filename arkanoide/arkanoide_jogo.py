#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *


''' TENTEI COMENTAR AO MAXIMO PARA FACILITAR O ENTENDIMENTO SE FALTOU ALGUM COMENTARIO ME AVISA QUE EU EXPLICO'''
''' PREPARAÇÃO DE TELA E CONSTANTES'''
LARGURA,ALTURA=800,800
'''
BARRA é a parte onde a bolinha bate e evita de cair
'''
BARRA=retangulo(60,10,Cor("red"))
'''
BOLA é a bolinha que percorre a tela destruindo os blocos
'''
BOLA=circulo(5,Cor("red"))
'''
BLOCO é a estrutura que sera destruida com  a bolinha
'''
BLOCO = carregar_imagem("images.jpg",40,20)
'''
SETA_ESQUERDA é o comando para fazer a barra ir para a esquerda quando apertar
'''
SETA_ESQUERDA = pg.K_LEFT
'''
SETA_DIREITA é o camando para fazer a barra ir para a direita quando apertar
'''
SETA_DIREITA = pg.K_RIGHT
'''
LIMITE_DIREITO é o limite de tela para evitar a barra e a bolinha de passar da tela
'''
LIMITE_DIREITO = 0 + LARGURA
'''
LIMITE_ESQUERDO é o limite de tela para evitar a barra e a bolinha de passar da tela
'''
LIMITE_ESQUERDO = LARGURA + BLOCO//2
'''
LIMITE BAIXO é para comparar quando a bolinha passou da barra e assim dar game over no jogo
'''
LIMITE_BAIXO = ALTURA
'''
LIMITE_CIMA é para impedir a bolinha de passar da tela por enquanto nao consegui uma ideia boa de fazer sem usar um numero por isso 
esta valendo 0 no momento
 '''
LIMITE_CIMA = 0





TELA = criar_tela_base(LARGURA , ALTURA)

Barra = definir_estrutura(" Barra " , " X , Y , DX ")
'''
Barra pode ser formada da seguinte forma:

'''
Bola = definir_estrutura(" Bola " , " X , Y , DX , DY ")
Bloco = definir_estrutura(" Bloco " , " X , Y ")

'''
!!!TODO!!!
'''
def quando_tick(Bola):
    return Bola






'''
#essa parte esta comentada para poder fazer as estruturas


#essa parte é para testar se a imagem esta sendo carregada na tela



TELA = criar_tela_base(400,400)

retan = retangulo(60,10,Cor("red"))


def desenhar(retan):
    return (colocar_imagem_sobre_tela_e_mostrar(retan,200,300))
'''