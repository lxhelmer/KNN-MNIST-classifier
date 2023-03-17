import unittest
from klahimmat import KLahimmat
from hausdorffvertailu import HausdorffVertailu
from lataaja import lataa_kuvat, lataa_nimikkeet
from data.pistejoukko_gen import pistejoukko, ruudut
import numpy as np
import tests.testi_arvot as arvot


class TestKNN(unittest.TestCase):

    def setUp(self):
        HV = HausdorffVertailu()
        self.tester_knn = KLahimmat(HV)

#Testaa knn valintaa kun kaikki arvot 0-9 tulevat äänestykseen.
#Todellisuudessa arrayn koko on 60t tuplea
    def test_knn_kaikki(self):
        test_array = [(0.1,1),(0.2,2),(0.3,3),(0.4,4),
                      (0.5,5),(0.6,6),(0.7,7),(0.8,8),
                      (0.9,9),(0.01,0)]
        self.assertEqual(self.tester_knn.knn_jarj(test_array,10),[1,1,1,1,1,1,1,1,1,1])

#Testaa että n tyypin alkioiden määrä lasketaan oikein muodostaessa yleisyys listaa
    def test_knn_4ykkosta(self):
        test_array = [(0.1,1),(0.2,1),(0.3,1),(0.4,1),
                      (0.5,5),(0.6,6),(0.7,7),(0.8,8),
                      (0.9,9),(0.01,0)]
        self.assertEqual(self.tester_knn.knn_jarj(test_array,10),[1,4,0,0,0,1,1,1,1,1])

#Testaa että k ollessa pienempi kuin arvioiden määrä vain k arviota otetaan huomioon
    def test_knn_4ykkostak5(self):
        test_array = [(0.01,0),(0.1,1),(0.2,1),(0.3,1),(0.4,1),
                      (0.5,5),(0.6,6),(0.7,7),(0.8,8),
                      (0.9,9)]
        self.assertEqual(self.tester_knn.knn_jarj(test_array,5),[1,4,0,0,0,0,0,0,0,0])

    def test_knn_4ykkostak4(self):
        test_array = [(0.1,1),(0.2,1),(0.3,1),(0.4,1),
                      (0.5,5),(0.6,6),(0.7,7),(0.8,8),
                      (0.9,9),(0.01,0)]
        self.assertEqual(self.tester_knn.knn_jarj(test_array,4),[1,3,0,0,0,0,0,0,0,0])
    
    def test_knn_sama(self):
        test_array = [(0.1,1),(0.2,1),(0.3,1),(0.4,1),
                      (0.1,5),(0.6,6),(0.7,7),(0.8,8),
                      (0.9,9),(0.01,0)]
        self.assertEqual(self.tester_knn.knn_jarj(test_array,5),[1,3,0,0,0,1,0,0,0,0])

    def test_knn(self):
        test_kuvat = np.array(
            [pistejoukko(x) for x in lataa_kuvat(arvot.HARJOITUS_POLKU)],
            dtype=object)
        test_ruud = harjoitusruudut = np.array(
            [ruudut(x) for x in lataa_kuvat(arvot.HARJOITUS_POLKU)])
        test_nimik = lataa_nimikkeet(arvot.HARJOITUS_POLKU)

        test_arvio = self.tester_knn.k_lahimmat(
                7,pistejoukko(arvot.A_mnist).tolist(),test_kuvat.tolist(),
                test_nimik.tolist(),test_ruud,ruudut(arvot.A_mnist).tolist()
                )
        self.assertEqual(test_arvio,9)
        self.assertEqual(self.tester_knn.yleisyys,[0,0,0,0,0,0,0,0,0,7])



        
