import unittest
import numpy as np
from data.pistejoukkoGen import pistejoukko, ruudut
from tests.testi_arvot import A_mnist, A_pisteet, A_ruudut


class TestPistejoukko(unittest.TestCase):
        
    def test_pistejoukko(self):
        np.testing.assert_array_equal(pistejoukko(A_mnist), A_pisteet)

    def test_ruudut(self):
        np.testing.assert_array_equal(ruudut(A_mnist), A_ruudut)
         
