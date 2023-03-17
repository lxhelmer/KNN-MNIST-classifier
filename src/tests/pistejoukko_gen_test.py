import unittest
import numpy as np
from data.pistejoukko_gen import pistejoukko, ruudut
from tests.testi_arvot import A_mnist, A_pisteet, A_ruudut, B_mnist, B_pisteet, B_ruudut


class TestPistejoukko(unittest.TestCase):

    def test_pistejoukko_A(self):
        np.testing.assert_array_equal(pistejoukko(A_mnist), A_pisteet)

    def test_ruudut_A(self):
        np.testing.assert_array_equal(ruudut(A_mnist), A_ruudut)

    def test_pistejoukko_B(self):
        np.testing.assert_array_equal(pistejoukko(B_mnist), B_pisteet)

    def test_ruudut_B(self):
        np.testing.assert_array_equal(ruudut(B_mnist), B_ruudut)

