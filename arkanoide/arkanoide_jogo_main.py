#!/usr/bin/env python
# -*- coding: utf-8 -*-


from arkanoide.arkanoide_jogo import *


''' ================= '''
''' Main (Big Bang):u89h
'''

''' Gato -> Gato '''
''' inicie o mundo com GATO_INICIAL '''


'''
peguei o layout do exemplo do gato que o professor tinha feito portando ainda precisa ser ajeitado para funcionar com o jogo
'''
def main(inic):
    big_bang(inic, frequencia=FREQUENCIA,
             quando_tick=mover_jogo,
             desenhar = desenha_jogo,
             quando_tecla = trata_tecla,
             quando_solta_tecla = solta_tecla,
             #quando_mouse= trata_mouse,
             #parar_quando=final_da_tela,
             modo_debug = True
    )


main(JOGO_INICIAL)   #chamando o main com estado iniaacial  =