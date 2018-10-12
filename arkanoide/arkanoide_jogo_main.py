#!/usr/bin/env python
# -*- coding: utf-8 -*-


from arkanoide.arkanoide_jogo import *


''' ================= '''
''' Main (Big Bang):
'''

''' Gato -> Gato '''
''' inicie o mundo com GATO_INICIAL '''


'''
peguei o layout do exemplo do gato que o professor tinha feito portando ainda precisa ser ajeitado para funcionar com o jogo
'''
def main(inic):
    big_bang(inic, frequencia=FREQUENCIA,
             quando_tick=mover,
             desenhar = desenha,
             quando_tecla = trata_tecla,
             #parar_quando=final_da_tela,
             modo_debug=True
    )


main(BARRA_INICIAL)   #chamando o main com estado inicial  = 0