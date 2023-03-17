import unittest
from tests.testi_arvot import A_pisteet, B_pisteet, A_ruudut, B_ruudut
from hausdorffvertailu import HausdorffVertailu
import math
import numpy as np
from data.pistejoukko_gen import ruudut

class TestHausdorff(unittest.TestCase):
    def setUp(self):
        self.test_hausdorff = HausdorffVertailu()

    def test_hausdorff_etaisyys(self):

        laskettu_etaisyys = 0.54655546181586
        test_etaisyys = self.test_hausdorff.m_hausdorff_etaisyys(A_pisteet, B_pisteet,
                                                            A_ruudut, B_ruudut)
        self.assertAlmostEqual(test_etaisyys, laskettu_etaisyys, 14)

    def test_hausdorff_samat(self):
        test_A = np.array([[1,1],[2,2],[3,3]])
        ruudut_test_A = np.zeros((28,28))
        ruudut_test_A[1,1] = 1
        ruudut_test_A[2,2] = 1
        ruudut_test_A[3,3] = 1
        ruudut_test_A = ruudut_test_A.astype(bool)

        test_etaisyys = self.test_hausdorff.m_hausdorff_etaisyys(
                test_A,test_A,
                ruudut_test_A,ruudut_test_A
                )

        self.assertEqual(test_etaisyys, 0) 

    def test_hausdorff_yhdenero(self):
        test_A = np.array([[1,1],[2,2],[3,3]])
        test_B = np.array([[1,1],[2,2]])
        ruudut_test_A = np.zeros((28,28))
        ruudut_test_A[1,1] = 1
        ruudut_test_A[2,2] = 1
        ruudut_test_A[3,3] = 1

        ruudut_test_B = np.zeros((28,28))
        ruudut_test_B[1,1] = 1
        ruudut_test_B[2,2] = 1
        ruudut_test_B = ruudut_test_B.astype(bool)
        ruudut_test_A = ruudut_test_A.astype(bool)

        test_etaisyys = self.test_hausdorff.m_hausdorff_etaisyys(
                test_A,test_B,
                ruudut_test_A,ruudut_test_B
                )
        self.assertEqual(test_etaisyys, math.sqrt(2)/3) 
