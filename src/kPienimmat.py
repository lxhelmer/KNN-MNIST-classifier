import heapq
class KPienimmat:

    def __init__(self,hausdorff):
        self._hausdorff_etaisyys = hausdorff.m_hausdorff_etaisyys

    def k_pienimmat(self, k, luokiteltava, harjoitusdata, harjoitusnimikkeet, ruudut_harjoitus, ruudut_luokiteltava):
        arvio_keko = []
        for kuva_indeksi in range(0,6000):
            if kuva_indeksi%1000 == 0:  #ohjelman etenemisen varmistamiseksi sekä silmämääräisen nopeuden arvioimiseksi
                print(kuva_indeksi)

            ero = self._hausdorff_etaisyys(luokiteltava, harjoitusdata[kuva_indeksi], ruudut_harjoitus[kuva_indeksi], ruudut_luokiteltava)

            if kuva_indeksi == 19:
                print("Käsinlasketun parin test 20, harj 19 ero " + str(ero))
                input()

            arvio_keko.append((ero, (harjoitusnimikkeet[kuva_indeksi][0])))
            
        heapq.heapify(arvio_keko)
        yleisimmat = []
        yleisyys = [0,0,0,0,0,0,0,0,0,0]

        for i in range(0, k):

            minimi = heapq.heappop(arvio_keko)
            yleisimmat.append(minimi)
            yleisyys[minimi[1]] = yleisyys[minimi[1]] +1
            print(minimi) #n pienin pari etäisyyden nousevassa järjestyksessä

            print(minimi[1]) #n pienimmän parin luokka

            print(yleisyys) #lista 0-9 arvojen määrästä

        yleisin = yleisyys.index(max(yleisyys)) #indeksi 0-9 jolla on korkein määrä

                
        return yleisin
