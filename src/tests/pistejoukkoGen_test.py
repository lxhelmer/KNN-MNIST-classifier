import unittest
import numpy as np
from data.pistejoukkoGen import pistejoukko, ruudut
from tests.testi_arvot import A_mnist, A_pisteet, A_ruudut


class TestPistejoukko(unittest.TestCase):
        
    def test_pistejoukko(self):
        self.assertEqual(pistejoukko(A_mnist), A_pisteet)

    def test_ruudut(self):
        self.assertEqual(ruudut(A_mnist), A_ruudut)
         
