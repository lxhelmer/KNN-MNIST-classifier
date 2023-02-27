import unittest
from tests.testi_arvot import A_pisteet, B_pisteet, A_ruudut, B_ruudut
from hausdorffvertailu import HausdorffVertailu






class TestHausdorff(unittest.TestCase):
    def setUp(self):
        pass

    def test_hausdorff_etaisyys(self):
            
            test_hausdorff = HausdorffVertailu()
            
            laskettu_etaisyys = 0.54655546181586
            test_etaisyys = test_hausdorff.m_hausdorff_etaisyys(A_pisteet, B_pisteet, A_ruudut, B_ruudut)
            self.assertAlmostEqual(test_etaisyys, laskettu_etaisyys, 14)

