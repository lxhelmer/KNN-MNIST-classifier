import heapq
import time
from multiprocessing import Process,Manager
class KPienimmat:

    def __init__(self,hausdorff):
        self._hausdorff_etaisyys = hausdorff.m_hausdorff_etaisyys

    def hd_kutsuja(self,alku,loppu):
        for kuva_indeksi in range(alku,loppu):
            ero = self._hausdorff_etaisyys(self._luokiteltava,
                                           self._harjoitusdata[kuva_indeksi],
                                           self._ruudut_luokiteltava,
                                           self._ruudut_harjoitus[kuva_indeksi])
            self.arvio_keko.append((ero, (self._harjoitusnimikkeet[kuva_indeksi])))


    def prosessit(self,arvio_keko, raja):
        self.prosessi1 = Process(target=self.hd_kutsuja,args=(0,int(raja/6)))
        self.prosessi2 = Process(target=self.hd_kutsuja,args=(int(raja/6),int(2*raja/6)))
        self.prosessi3 = Process(target=self.hd_kutsuja,args=(int(2*raja/6),int(3*raja/6)))
        self.prosessi4 = Process(target=self.hd_kutsuja,args=(int(3*raja/6),int(4*raja/6)))
        self.prosessi5 = Process(target=self.hd_kutsuja,args=(int(4*raja/6),int(5*raja/6)))
        self.prosessi6 = Process(target=self.hd_kutsuja,args=(int(5*raja/6),raja))
        

        self.prosessi1.start()
        self.prosessi2.start()
        self.prosessi3.start()
        self.prosessi4.start()
        self.prosessi5.start()
        self.prosessi6.start()

        

    def k_pienimmat(self, k, luokiteltava, harjoitusdata, harjoitusnimikkeet, ruudut_harjoitus, ruudut_luokiteltava):
        self._luokiteltava = luokiteltava
        self._harjoitusdata = harjoitusdata
        self._harjoitusnimikkeet = harjoitusnimikkeet
        self._ruudut_harjoitus = ruudut_harjoitus
        self._ruudut_luokiteltava = ruudut_luokiteltava

        lista_ctrl = Manager()
        self.arvio_keko = lista_ctrl.list()

        self.prosessit(self.arvio_keko,60000)

        self.prosessi1.join()
        self.prosessi2.join()
        self.prosessi3.join()
        self.prosessi4.join()
        self.prosessi5.join()
        self.prosessi6.join()
        

       # for kuva_indeksi in range(0,6000):
       #     if (kuva_indeksi%1000==0):
       #         print(str(kuva_indeksi))
       #     ero = self._hausdorff_etaisyys(luokiteltava, harjoitusdata[kuva_indeksi],ruudut_luokiteltava, ruudut_harjoitus[kuva_indeksi])

       #     arvio_keko.append((ero, (harjoitusnimikkeet[kuva_indeksi])))
            
        aito_lista = list(self.arvio_keko)
        knn_alku = time.time()
        heapq.heapify(aito_lista)
        yleisimmat = []
        yleisyys = [0,0,0,0,0,0,0,0,0,0]
        
        for i in range(0, k):

            minimi = heapq.heappop(aito_lista)
            yleisimmat.append(minimi)
            yleisyys[minimi[1]] = yleisyys[minimi[1]] +1
            print(minimi) #n pienin pari etäisyyden nousevassa järjestyksessä


        print(yleisyys) #lista 0-9 arvojen määrästä

        yleisin = yleisyys.index(max(yleisyys)) #indeksi 0-9 jolla on korkein määrä
        
        knn_loppu = time.time()
        print("knn sort time: " + str(knn_loppu-knn_alku))
                
        return yleisin
