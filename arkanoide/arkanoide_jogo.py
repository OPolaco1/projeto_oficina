#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *

''' JOGO DO ARKANOID'''

'''============================================================='''
''' PREPARAÇÃO DE TELA E CONSTANTES'''
FREQUENCIA = 60

LARGURA,ALTURA = 800,800

TELA = criar_tela_base(LARGURA,ALTURA)

IMG_BARRA = carregar_imagem("barra.png", 150, 30)
IMG_BOLA  = carregar_imagem("bolinha.png", 150, 100)
IMG_BLOCO = carregar_imagem("bloco.jpg", 80, 20)
GAME_OVER = carregar_imagem("game_over.png", 400, 400)
WIN = carregar_imagem("win.png", 400, 400)



SETA_ESQUERDA = pg.K_a
SETA_DIREITA = pg.K_d
ESPACO = pg.K_SPACE
LIMITE_ESQUERDO = 0 + largura_imagem(IMG_BOLA) // 4
LIMITE_DIREITO = LARGURA - largura_imagem(IMG_BOLA) // 4
LIMITE_BAIXO = ALTURA - altura_imagem(IMG_BOLA) // 4
LIMITE_CIMA = 0 + altura_imagem(IMG_BOLA) // 4
Y = ALTURA // 2 + LARGURA // 2.5


Bloco = definir_estrutura("bloco","x y")

BLOCO1 = Bloco(440, 220)
BLOCO2 = Bloco(520, 220)
BLOCO3 = Bloco(600, 220)
BLOCO4 = Bloco(520, 200)
BLOCO5 = Bloco(200, 200)
BLOCO6 = Bloco(280, 200)
BLOCO7 = Bloco(680, 220)
BLOCO8 = Bloco(40, 200)
BLOCO9 = Bloco(120, 200)
BLOCO10 = Bloco(360, 200)
BLOCO11 = Bloco(440, 200)
BLOCO12 = Bloco(600,200)
BLOCO13 = Bloco(680,200)
BLOCO14 = Bloco(760,200)
BLOCO15 = Bloco(40,220)
BLOCO16 = Bloco(120,220)
BLOCO17 = Bloco(200,220)
BLOCO18 = Bloco(280,220)
BLOCO19 = Bloco(360,220)
BLOCO20 = Bloco(760,220)
BLOCO21 = Bloco(40,240)
BLOCO22 = Bloco(120,240)
BLOCO23 = Bloco(200,240)
BLOCO24 = Bloco(280,240)
BLOCO25 = Bloco(360,240)
BLOCO26 = Bloco(440,240)
BLOCO27 = Bloco(520,240)
BLOCO28 = Bloco(600,240)
BLOCO29 = Bloco(680,240)
BLOCO30 = Bloco(760,240)
BLOCO31 = Bloco(40,260)
BLOCO32 = Bloco(120,260)
BLOCO33 = Bloco(200,260)
BLOCO34 = Bloco(280,260)
BLOCO35 = Bloco(360,260)
BLOCO36 = Bloco(440,260)
BLOCO37 = Bloco(520,260)
BLOCO38 = Bloco(600,260)
BLOCO39 = Bloco(680,260)
BLOCO40 = Bloco(760,260)
BLOCO41 = Bloco(40,280)
BLOCO42 = Bloco(120,280)
BLOCO43 = Bloco(200,280)
BLOCO44 = Bloco(280,280)
BLOCO45 = Bloco(360,280)
BLOCO46 = Bloco(440,280)
BLOCO47 = Bloco(520,280)
BLOCO48 = Bloco(600,280)
BLOCO49 = Bloco(680,280)
BLOCO50 = Bloco(760,280)
BLOCO51 = Bloco(40,300)
BLOCO52 = Bloco(120,300)
BLOCO53 = Bloco(200,300)
BLOCO54 = Bloco(280,300)
BLOCO55 = Bloco(360,300)
BLOCO56 = Bloco(440,300)
BLOCO57 = Bloco(520,300)
BLOCO58 = Bloco(600,300)
BLOCO59 = Bloco(680,300)
BLOCO60 = Bloco(760,300)
LISTA = [BLOCO1, BLOCO2, BLOCO3, BLOCO4, BLOCO5, BLOCO6, BLOCO7, BLOCO8, BLOCO9, BLOCO10, BLOCO11, BLOCO12, BLOCO13, BLOCO14, \
         BLOCO15,BLOCO16,BLOCO17,BLOCO18,BLOCO19,BLOCO20,BLOCO21,BLOCO22,BLOCO23,BLOCO24,BLOCO25,BLOCO26,BLOCO27,BLOCO28,BLOCO29,\
         BLOCO30,BLOCO31,BLOCO32,BLOCO33,BLOCO34,BLOCO35,BLOCO36,BLOCO37,BLOCO38,BLOCO39,BLOCO40,BLOCO41,BLOCO42,BLOCO43,BLOCO44,\
         BLOCO45,BLOCO46,BLOCO47,BLOCO48,BLOCO49,BLOCO50,BLOCO51,BLOCO52,BLOCO53,BLOCO54,BLOCO55,BLOCO56,BLOCO57,BLOCO58,BLOCO59,BLOCO60]

METADE_L_BLOCO = largura_imagem(IMG_BLOCO) // 2
METADE_A_BLOCO = altura_imagem(IMG_BLOCO) // 2

# ListaBlocos
LISTA2 = [BLOCO4]


Barra = definir_estrutura("barra","x y dx tam")
BARRA_INICIAL = Barra(LARGURA // 2, Y, 0, 150)

Bola = definir_estrutura("bola","x dx y dy")
BOLA_INICIAL = Bola(BARRA_INICIAL.x, 0, Y - altura_imagem(IMG_BARRA)//2 , 0)
DX = 6

ALTURA_BOLA = altura_imagem(IMG_BOLA) // 2


# def novos_blocos():
#     for x in range(50, 750,largura_imagem(IMG_BLOCO)):
#         for y in range(200, 300,altura_imagem(IMG_BLOCO)):
#             novo_bloco = Bloco(x, y)
#             y = y + 20
#
#             lista = [novo_bloco]
#         x = x + 50
#         return lista
#
#
# NOVA_LISTA = novos_blocos()

Jogo = definir_estrutura("jogo", "barra bola blocos game_over")
JOGO_INICIAL = Jogo(BARRA_INICIAL, BOLA_INICIAL, LISTA, False)
'''
as condicionais da função desenha serve para limitar o movimento da barra para nao ultrapassar os limites da tela
'''
'''========================'''
''' DEFINIÇÃO DE DADOS'''
def desenha_barra(barra):
    nova_barra = definir_dimensoes(IMG_BARRA,barra.tam,30)
    if (barra.x < LIMITE_DIREITO and barra.x > LIMITE_ESQUERDO):
        colocar_imagem(nova_barra,TELA,barra.x,Y)
    elif (barra.x <= LIMITE_DIREITO):
        colocar_imagem(nova_barra,TELA,LIMITE_ESQUERDO,Y)
    elif (barra.x >= LIMITE_ESQUERDO):
        colocar_imagem(nova_barra,TELA,LIMITE_DIREITO,Y)

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
    return Jogo(nova_barra, nova_bola,jogo.blocos,False)




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
        return Barra(LIMITE_ESQUERDO, Y, barra.dx, barra.tam)
    elif(barra.x > LIMITE_DIREITO):
        return Barra(LIMITE_DIREITO, Y, barra.dx, barra.tam)
    '''
    caso passe das comparações acima ele ira comparar qual tecla foi clicada para mover a barra para a direção certa
    obs ainda nao consegui fazer a barra mexer simplesmente segurando a tecla tem q aperfeiçoar isso 
    '''
    if tecla == SETA_ESQUERDA:
        return Barra(barra.x, Y, barra.dx - 10, barra.tam)
    elif tecla == SETA_DIREITA:
        return Barra(barra.x, Y, barra.dx + 10, barra.tam)
        #else
    return barra



def colide_bola(bola,barra):
    lado_esquerdo = barra.x - barra.tam // 2
    lado_direito = barra.x + barra.tam // 2
    if bola.x <= lado_direito and bola.x >= lado_esquerdo and bola.y >= Y - altura_imagem(IMG_BARRA)//2:

        if lado_esquerdo <= bola.x and bola.x <= lado_esquerdo + barra.tam // 3:
            if bola.dx == 0:
                return 1
            else:
                return 2

        if lado_direito >= bola.x and bola.x >= lado_direito - barra.tam // 3:
            if bola.dx == 0:
                return 3
            else:
                return 4

        return 5
    else:
        return 0










    #     if nova_bola_y > Y + altura_imagem(IMG_BARRA)/1.5:
    #         if nova_bola_x <=  limite_barra_esquerdo:
    #             if bola.x == 0:
    #                 return 1 #Bola(nova_bola_x,-bola.dy,bola.y,-bola.dy)
    #             else:
    #                 return 2 #Bola(nova_bola_x,0,bola.y,-bola.dy)
    #
    #         if nova_bola_x >= limite_barra_direito:
    #             if bola.x == 0:
    #                 return 3 #Bola(nova_bola_x, +bola.dy, bola.y, -bola.dy)
    #             else:
    #                 return 4 #Bola(nova_bola_x, 0, bola.y, -bola.dy)
    #         return 5 #Bola(bola.x,bola.dx,nova_bola_y,-bola.dy)
    #
    #
    # #return nova_bola_y > Y - altura_imagem(IMG_BARRA) //1.5


def mover_bola(bola):
    nova_bola_y = bola.y - bola.dy
    nova_bola_x = bola.x - bola.dx

    if nova_bola_y < 0 + altura_imagem(IMG_BOLA):
        return Bola(nova_bola_x, bola.dx, nova_bola_y, -(bola.dy+0.5))
    if nova_bola_x < LIMITE_ESQUERDO or nova_bola_x > LIMITE_DIREITO:
        return Bola(nova_bola_x, -(bola.dx), nova_bola_y, bola.dy)
    # if nova_bola_x < 0 + altura_imagem(IMG_BOLA):
    #     return Bola(nova_bola_x,-bola.dx,bola.y,bola.dy)
    # if nova_bola_x

    return Bola(nova_bola_x,bola.dx,nova_bola_y,bola.dy)


def mover_barra(barra):

    posicao = barra.x + barra.dx
    return Barra(posicao, Y, barra.dx,barra.tam)


def solta_tecla(jogo, tecla):
    nova_barra = solta_tecla_barra(jogo.barra,tecla)
    return Jogo(nova_barra, jogo.bola,jogo.blocos, False)

def solta_tecla_barra(barra, tecla):
    if SETA_DIREITA == tecla or SETA_ESQUERDA == tecla:

        return Barra(barra.x, Y, 0,barra.tam)
    return barra


def bola_parada(bola):
    return (bola.dx == 0 and bola.dy == 0)


def desenha_bloco(bloco):
    colocar_imagem(IMG_BLOCO,TELA,bloco.x,bloco.y)

def desenha_blocos(blocos):
    for bloco in blocos:
        desenha_bloco(bloco)



def game_over(bola):
    return bola.y >= ALTURA

def colide_bloco(bola,bloco):
    limite_bloco_cima = bloco.y - METADE_A_BLOCO
    limite_bloco_baixo = bloco.y + METADE_A_BLOCO
    limite_bloco_esquerda = bloco.x - METADE_L_BLOCO
    limite_bloco_direita = bloco.x + METADE_L_BLOCO

    if limite_bloco_baixo >= bola.y and \
        limite_bloco_cima <= bola.y and \
        limite_bloco_direita >= bola.x and \
        limite_bloco_esquerda <= bola.x:
        return bloco
    return False


def colide_blocos(bola,blocos):
    for bloco in blocos:
        exclui_bloco = colide_bloco(bola,bloco)
        if exclui_bloco:
            return exclui_bloco

# def inverte_bola1(bola, blocos):
#     for bloco in blocos:
#         nova_bola = inverte_bola(bola, bloco)
#         return nova_bola

def inverte_bola(bola,bloco):

    lado_esquerdo = bloco.x - largura_imagem(IMG_BLOCO) // 2
    lado_direito = bloco.x + largura_imagem(IMG_BLOCO) // 2
    lado_cima = bloco.y - altura_imagem(IMG_BLOCO) // 2
    lado_baixo = bloco.y + altura_imagem(IMG_BLOCO) // 2
    # limite_bloco_cima = bloco.y - METADE_A_BLOCO
    # limite_bloco_baixo = bloco.y + METADE_A_BLOCO
    # limite_bloco_esquerda = bloco.x - METADE_L_BLOCO
    # limite_bloco_direita = bloco.x + METADE_L_BLOCO

    if lado_baixo <= bola.y and lado_cima >= bola.y:
        return Bola(bola.x, -bola.dx, bola.y, bola.dy)

    if lado_direito >= bola.x and  lado_esquerdo <= bola.x :
        return Bola(bola.x, bola.dx, bola.y, -bola.dy)
    return Bola(bola.x, bola.dx, bola.y, bola.dy)


    #
    # if limite_bloco_baixo >= bola.y and \aaa
    #         limite_bloco_cima <= bola.y and \
    #         limite_bloco_direita >= bola.x and \
    #         limite_bloco_esquerda <= bola.x:
    #


    # limite_bloco_cima = bloco.y - METADE_A_BLOCO
    # limite_bloco_baixo = bloco.y + METADE_A_BLOCO
    # limite_bloco_esquerda = bloco.x - METADE_L_BLOCO
    # limite_bloco_direita = bloco.x + METADE_L_BLOCO
    #
    # # if bola == 1:
    # #     nova_bola = Bola(nova_bola.x, nova_bola.dx, nova_bola.y, -nova_bola.dy)
    # # if nova_bola == 2:
    # #     bola = bola(bola.x, -dx, bola.y, bola.dy)
    #
    # if limite_bloco_baixo >= bola.y and limite_bloco_cima <= bola.y:
    #     return bola(bola.x, bola.dx, bola.y, -bola.dy)
    # if limite_bloco_esquerda <= bola.x and limite_bloco_direita >= bola.x:
    #     return bola(bola.x, -bola.dx, bola.y, bola.dy)



def mover_jogo(jogo):
    if(not game_over(jogo.bola)):
        nova_barra = mover_barra(jogo.barra)

        if bola_parada(jogo.bola):

            nova_bola = Bola(jogo.barra.x, jogo.bola.dx, jogo.bola.y, jogo.bola.dy)
        else:
            nova_bola = mover_bola(jogo.bola)
        colisao = colide_bola(nova_bola,jogo.barra)
        if colisao == 1:
            nova_bola = Bola(nova_bola.x, DX, nova_bola.y,-nova_bola.dy)
        elif colisao == 2:
            nova_bola = Bola(nova_bola.x, 0, nova_bola.y,-nova_bola.dy)
        elif colisao == 3:
            nova_bola = Bola(nova_bola.x, -DX, nova_bola.y, -nova_bola.dy)
        elif colisao == 4:
            nova_bola = Bola(nova_bola.x, 0, nova_bola.y, -nova_bola.dy)
        elif colisao == 5:
            nova_bola = Bola(nova_bola.x, nova_bola.dx, nova_bola.y, -nova_bola.dy)

        exclui_bloco = colide_blocos(jogo.bola,jogo.blocos)
        if exclui_bloco:
            bola = inverte_bola(jogo.bola, exclui_bloco)

            novos_blocos = [bloco for bloco in jogo.blocos if bloco != exclui_bloco]
            return Jogo(nova_barra, bola, novos_blocos, False)

        return Jogo(nova_barra, nova_bola,jogo.blocos, False)

    return Jogo(jogo.barra,jogo.bola,jogo.blocos, True)


def desenha_game_over():
    colocar_imagem(GAME_OVER, TELA, 400, 400)

def desenha_win():
    carregar_imagem(WIN, TELA, 400, 400)

def desenha_jogo(jogo):
    if (not jogo.game_over):
        desenha_barra(jogo.barra)
        desenha_bola(jogo.bola)
        desenha_blocos(jogo.blocos)
        if jogo.blocos == []:
            desenha_win()
    else:
        return desenha_game_over()

