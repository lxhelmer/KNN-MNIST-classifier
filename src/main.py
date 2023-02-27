import time
import numpy as np
import random
from lataaja import lataa_kuvat, lataa_nimikkeet
from data.pistejoukkoGen import pistejoukko, ruudut 
from data.csvKaantaja import CsvKaantaja
from hausdorffvertailu import HausdorffVertailu
from kPienimmat import KPienimmat
from ui.piirrin import Piirrin

harjoitus_polku = "../../train/train-"
testi_polku = "../../test/t10k-"




def raportti(oikein, n, i, tulokset, ruudut, aika, piirrin):
    print(">"*20)
    
    print("Arvioon käytetty aika: " + str(aika))
    if oikein != 0:
        print("Kokonais tarkkuus: " + str(oikein/n))
    print("Arvio: " + str(tulokset[n-1][0]))
    print("Todellinen: " + str(tulokset[n-1][1]))
    print("<"*20)

    
def main():
    hausdorff = HausdorffVertailu()
    knn = KPienimmat(hausdorff)
    csvk = CsvKaantaja()
    piirrin = Piirrin()



    k = 11          # määritetään k arvo
                                                                        #ladataan csv tiedostoista harjoitusdata runtime listoihin.
    harjoitusdata = csvk.lue_tiedostosta("kordinaatit.csv")             #harjoitusdata on 2D lista jossa jokainen rivi on [y,x] kordinaattipari (lista) 
    harjoitusnimikkeet = csvk.lue_tiedostosta("nimikkeet.csv")          #nimikkeet ovat normaali lista
    harjoitusruudut = csvk.lue_tiedostosta("ruudut.csv")                #ruudut ovat 3D lista jossa jokainen rivi sisältää 28x28 2D listan
                                                                        #tämä 2D listan kohdassa [y][x] on kyseisen pisteen pixelin totuusarvo(boolean)


    testinimikkeet = lataa_nimikkeet(testi_polku)                       #ladataan testinimikkeet normaali lista

    tulokset = []
    oikein = 0
    luok_num = 20 
    #piirrin.piirra_pistejoukko(pistejoukko(lataa_kuvat(testi_polku)[luok_num]))
    #piirrin.piirra_pistejoukko(pistejoukko(lataa_kuvat(harjoitus_polku)[luok_num-1]))

    #random.randint(0,9999)                                   #valitaan indeksi testikuvalle. Kuvien arvioinnin absoluuttinen nopeus vaihtelee
                                                                        #eri kuvien välillä joten on hyvä testata eri kuvilla.


    for i in range(luok_num,luok_num+11):                                #arvioidaan yksi kuva, rakenne helposti muutettavissa tarkkuuden arviointiin.
        luokiteltava_mnist = lataa_kuvat(testi_polku)[i]                #ladataan mnist ubyte tiedostosta mnist pixeli toteutus kuvasta.
        luokiteltava = pistejoukko(luokiteltava_mnist)                  #luodaan pixelitoteutuksesta kordinaatti joukko
        luokiteltava_ruudut = ruudut(luokiteltava_mnist)
        

        print("alkaa")
        alku_aika = time.time()

        arvio = knn.k_pienimmat(                                        #arvioidaan luokiteltavan kuvan nimike
                k,
                luokiteltava,
                harjoitusdata,
                harjoitusnimikkeet,
                harjoitusruudut,
                luokiteltava_ruudut)                                    #yksittäinen 2D lista toisin kuin harjoitus ruudut
        
        loppu_aika = time.time()

        
        tulokset.append([arvio,testinimikkeet[i]])
        
        if arvio == testinimikkeet[i]:
            oikein += 1


        raportti(oikein, i-luok_num+1, i, tulokset, luokiteltava_ruudut, loppu_aika-alku_aika, piirrin)

    for res in tulokset:
        print("Arvioitu luku: " + str(res[0]) + " | Todellinen luku: " + str(res[1]),end="")
        if res[0] == res[1]:
            print(" |  SAMA!!!")
        else:
            print("")



if __name__ == "__main__":
    main()


