import heapq
import time
from multiprocessing import Manager
from .prosessit import prosessit

class KLahimmat:

    def __init__(self,hausdorff):
        self._hausdorff_etaisyys = hausdorff.m_hausdorff_etaisyys
        self._luokiteltava = None
        self._harjoitusdata = None
        self._harjoitusnimikkeet = None
        self._ruudut_harjoitus = None
        self._ruudut_luokiteltava = None
        self._lista_ctrl = Manager()
        self.prosessi_lista = None

    #Hd etäisyyksiä laskeva funktio jota prosessit ajavat eri väleillä.
    def hd_kutsuja(self,alku,loppu):
        for kuva_indeksi in range(alku,loppu):
            ero = self._hausdorff_etaisyys(self._luokiteltava,
                                           self._harjoitusdata[kuva_indeksi],
                                           self._ruudut_luokiteltava,
                                           self._ruudut_harjoitus[kuva_indeksi])
            self.prosessi_lista.append((ero, (self._harjoitusnimikkeet[kuva_indeksi])))

    #Funktio luo yleisyys listan jonka indeksi n kuvaa luvun n määrää k pienimpiä
    #etäisyyksiä vastaavien nimikkeiden joukossa

    def knn_jarjestaja(self, arvo_parit,k):
        heapq.heapify(arvo_parit)
        yleisimmat = []
        yleisyys = [0,0,0,0,0,0,0,0,0,0]

        for i in range(0, k):
            minimi = heapq.heappop(arvo_parit)
            yleisimmat.append(minimi)
            yleisyys[minimi[1]] = yleisyys[minimi[1]] + 1
            print(minimi) #n pienin pari etäisyyden nousevassa järjestyksessä

        print(yleisyys) #lista 0-9 arvojen määrästä

        return yleisyys

    def k_lahimmat(self,k, luokiteltava,
                    harjoitusdata, harjoitusnimikkeet,
                    ruudut_harjoitus, ruudut_luokiteltava
                    ):

        self._luokiteltava = luokiteltava
        self._harjoitusdata = harjoitusdata
        self._harjoitusnimikkeet = harjoitusnimikkeet
        self._ruudut_harjoitus = ruudut_harjoitus
        self._ruudut_luokiteltava = ruudut_luokiteltava
        self.prosessi_lista = self._lista_ctrl.list()

        prosessit(60000, self.hd_kutsuja) #Käynnistetään prosessit

        keko_lista = list(self.prosessi_lista) #Luodaan prosessien yhteislistasta normaali lista.

        knn_alku = time.time()

        self.yleisyys = self.knn_jarjestaja(keko_lista,k)
        maksimi_maara = max(self.yleisyys)
        yleisin = self.yleisyys.index(maksimi_maara) #valitaan indeksi 0-9 jolla on korkein määrä

        knn_loppu = time.time()

        print("knn sort time: " + str(knn_loppu-knn_alku))
        print("Varmuus: ", str(maksimi_maara/k))

        return yleisin
