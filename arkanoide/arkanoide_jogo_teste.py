#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest



from arkanoide.arkanoide_jogo import *



class Test(unittest.TestCase):
    def testcolide_bola(self):
        self.assertEqual(colide_bola(Bola(400, 0, 150, 6), BARRA_INICIAL), 0)
        self.assertEqual(colide_bola(Bola(BARRA_INICIAL.x - BARRA_INICIAL.tam / 2 - 1, 0, Y - altura_imagem(IMG_BARRA)//2, 6), BARRA_INICIAL),1)