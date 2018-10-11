#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from htdp_pt_br.universe import *

from arkanoide.arkanoide_jogo import *



class Test(unittest.TestCase):

    def trata_tecla_test(self):
        self.assertEqual(trata_tecla(SETA_ESQUERDA),-3)