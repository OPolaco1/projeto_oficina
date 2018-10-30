#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *

FREQUENCIA = 60

LARGURA,ALTURA = 800,800

TELA = criar_tela_base(LARGURA,ALTURA)

IMG_BARRA = carregar_imagem("barra.png", 150, 30)
IMG_BOLA  = carregar_imagem("bolinha.png", 150, 100)
IMG_BLOCO = carregar_imagem("bloco.jpg", 80, 20)



SETA_ESQUERDA = pg.K_a
SETA_DIREITA = pg.K_d
ESPACO = pg.K_SPACE
LIMITE_ESQUERDO = 0 + largura_imagem(IMG_BOLA) // 4
LIMITE_DIREITO = LARGURA - largura_imagem(IMG_BOLA) // 4
LIMITE_BAIXO = ALTURA - altura_imagem(IMG_BOLA) // 4
LIMITE_CIMA = 0 + altura_imagem(IMG_BOLA) // 4
Y = ALTURA // 2 + LARGURA // 2.5



Barra = definir_estrutura("barra","x y dx")
BARRA_INICIAL = Barra(LARGURA // 2, Y, 0)

Bola = definir_estrutura("bola","x dx y dy")
BOLA_INICIAL = Bola(BARRA_INICIAL.x, 0, Y - altura_imagem(IMG_BARRA)//2 , 0)

Jogo = definir_estrutura("jogo", "barra bola game_over")
JOGO_INICIAL = Jogo(BARRA_INICIAL, BOLA_INICIAL, False)
'''
as condicionais da função desenha serve para limitar o movimento da barra para nao ultrapassar os limites da tela
'''
def desenha_barra(barra):
    if (barra.x < LIMITE_DIREITO and barra.x > LIMITE_ESQUERDO):
        colocar_imagem(IMG_BARRA,TELA,barra.x,Y)
    elif (barra.x <= LIMITE_DIREITO):
        colocar_imagem(IMG_BARRA,TELA,LIMITE_ESQUERDO,Y)
    elif (barra.x >= LIMITE_ESQUERDO):
        colocar_imagem(IMG_BARRA,TELA,LIMITE_DIREITO,Y)

def desenha_bola(bola):
    if bola.x < LIMITE_DIREITO and bola.x > LIMITE_ESQUERDO and bola.y > LIMITE_CIMA and bola.y < LIMITE_BAIXO:
        colocar_imagem(IMG_BOLA,TELA, bola.x, bola.y)


def trata_tecla_bola(bola,tecla):
    if tecla ==pg.K_SPACE:
        return Bola(bola.x, 0, bola.y, 6)
    return bola

def trata_tecla(jogo,tecla):
    nova_barra = trata_tecla_barra(jogo.barra,tecla)
    nova_bola = trata_tecla_bola(jogo.bola,tecla)
    return Jogo(nova_barra, nova_bola,False)




def trata_tecla_barra(barra,tecla):
    '''

    :param barra:
    :param tecla:
    :return:
    '''
    '''   
    comparação para limitar a barra aos limites laterais impedindo assim que a barra suma da tela
    '''

    if(barra.x < LIMITE_ESQUERDO):
        return Barra(LIMITE_ESQUERDO,Y)
    elif(barra.x > LIMITE_DIREITO):
        return Barra(LIMITE_DIREITO,Y)
    '''
    caso passe das comparações acima ele ira comparar qual tecla foi clicada para mover a barra para a direção certa
    obs ainda nao consegui fazer a barra mexer simplesmente segurando a tecla tem q aperfeiçoar isso 
    '''
    if tecla == SETA_ESQUERDA:
        return Barra(barra.x, Y,barra.dx -3)
    elif tecla == SETA_DIREITA:
        return Barra(barra.x, Y, barra.dx +3)
        #else
    return barra


def mover_bola(bola):
    nova_bola = bola.y - bola.dy
    if nova_bola < 0 + altura_imagem(IMG_BOLA):
        return Bola(bola.x,bola.dx,nova_bola,-(bola.dy+0.5))
    if nova_bola < LIMITE_ESQUERDO or nova_bola > LIMITE_DIREITO:
        return Bola(bola.x,-bola.dx,nova_bola,bola.dy)
    return Bola(bola.x,bola.dx,nova_bola,bola.dy)


def mover_barra(barra):

    posicao = barra.x + barra.dx
    return Barra(posicao, Y, barra.dx)


def solta_tecla(jogo, tecla):
    nova_barra = solta_tecla_barra(jogo.barra,tecla)
    return Jogo(nova_barra, jogo.bola, False)

def solta_tecla_barra(barra, tecla):
    if SETA_DIREITA == tecla or SETA_ESQUERDA == tecla:

        return Barra(barra.x, Y, 0)
    return barra


def bola_parada(bola):
    return (bola.dx == 0 and bola.dy == 0)


def game_over(bola):
    return bola.y >= ALTURA



def mover_jogo(jogo):
    if(not game_over(jogo.bola)):
        nova_barra = mover_barra(jogo.barra)

        if bola_parada(jogo.bola):

            nova_bola = Bola(jogo.barra.x, jogo.bola.dx, jogo.bola.y, jogo.bola.dy)
        else:
            nova_bola = mover_bola(jogo.bola)
        return Jogo(nova_barra, nova_bola, False)
    return Jogo(jogo.barra,jogo.bola, True)




def desenha_jogo(jogo):
    if (not jogo.game_over):
        desenha_barra(jogo.barra)
        desenha_bola(jogo.bola)
    else:
        return jogo

#print(BARRA_INICIAL)
'''


Barra pode ser formada por: Int[

'''

'''
retan = IMG_BOLA


def desenhar(retan):
    return colocar_imagem_sobre_tela_e_mostrar(retan,400,700)



desenhar(retan)

'''