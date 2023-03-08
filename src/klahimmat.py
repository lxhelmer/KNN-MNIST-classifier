import heapq
import time
from multiprocessing import Manager
from prosessit import prosessit

class KLahimmat:

    def __init__(self,hausdorff):
        self._hausdorff_etaisyys = hausdorff.m_hausdorff_etaisyys
        self._luokiteltava = None
        self._harjoitusdata = None
        self._harjoitusnimikkeet = None
        self._ruudut_harjoitus = None
        self._ruudut_luokiteltava = None
        self.lista_ctrl = Manager()
        self.prosessi_lista = None

    #Hd etäisyyksiä laskeva funktio jota prosessit ajavat eri väleillä.
    def hd_kutsuja(self,alku,loppu):
        for kuva_indeksi in range(alku,loppu):
            ero = self._hausdorff_etaisyys(self._luokiteltava,
                                           self._harjoitusdata[kuva_indeksi],
                                           self._ruudut_luokiteltava,
                                           self._ruudut_harjoitus[kuva_indeksi])
            self.prosessi_lista.append((ero, (self._harjoitusnimikkeet[kuva_indeksi])))

    def k_lahimmat(self,k, luokiteltava,
                    harjoitusdata, harjoitusnimikkeet,
                    ruudut_harjoitus, ruudut_luokiteltava
                    ):
        self._luokiteltava = luokiteltava
        self._harjoitusdata = harjoitusdata
        self._harjoitusnimikkeet = harjoitusnimikkeet
        self._ruudut_harjoitus = ruudut_harjoitus
        self._ruudut_luokiteltava = ruudut_luokiteltava
        self.prosessi_lista = self.lista_ctrl.list()

        prosessit(60000, self.hd_kutsuja)

        keko_lista = list(self.prosessi_lista)

        knn_alku = time.time()

        heapq.heapify(keko_lista)
        yleisimmat = []
        yleisyys = [0,0,0,0,0,0,0,0,0,0]

        for i in range(0, k):
            minimi = heapq.heappop(keko_lista)
            yleisimmat.append(minimi)
            yleisyys[minimi[1]] = yleisyys[minimi[1]] +1
            print(minimi) #n pienin pari etäisyyden nousevassa järjestyksessä


        print(yleisyys) #lista 0-9 arvojen määrästä
        
        maksimi = max(yleisyys)
        yleisin = yleisyys.index(maksimi) #indeksi 0-9 jolla on korkein määrä


        knn_loppu = time.time()
        print("knn sort time: " + str(knn_loppu-knn_alku))
        print("Varmuus: ", str(maksimi/k))

        return yleisin
