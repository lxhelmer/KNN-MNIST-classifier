import heapq
from hausdorffvertailu import m_hausdorff_etaisyys


def k_pienimmat(k, luokiteltava, harjoitusdata, harjoitusnimikkeet):
    arvio_keko = []
    for kuva_indeksi in range(0,10000):
        ero = m_hausdorff_etaisyys(luokiteltava, harjoitusdata[kuva_indeksi])

        #vertailut[ero] = harjoitusnimikkeet[kuva_indeksi]
        arvio_keko.append((ero, (harjoitusnimikkeet[kuva_indeksi][0])))
        #print(ero, harjoitusnimikkeet[kuva_indeksi][0])
        
        #print(kuva_indeksi)
        #print("-")
    
    heapq.heapify(arvio_keko)
    yleisimmat = []
    yleisyys = [0,0,0,0,0,0,0,0,0,0]

    for i in range(0, k):
        minimi = heapq.heappop(arvio_keko)
        print(minimi)
        print(minimi[1])
        print(yleisyys)
        yleisimmat.append(minimi)
        yleisyys[minimi[1]] = yleisyys[minimi[1]] +1


    yleisin = yleisyys.index(max(yleisyys))

            
    return yleisin
