#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *

'''
este arquivo é para criar os retangulos que serão destruidos pelas bolinhas

'''


TELA=criar_tela_base(400,400)

retan=retangulo(60,10,Cor("red"))


def desenhar(retan):
    return (colocar_imagem_sobre_tela_e_mostrar(retan,200,300))

