import os
import time
#import matplotlib.pyplot as plt
import numpy as np
import struct
import random
from data.pistejoukkoGen import pistejoukko, ruudut 
from data.csvKaantaja import CsvKaantaja
from hausdorffvertailu import HausdorffVertailu
from kPienimmat import KPienimmat
from ui.piirrin import Piirrin

harjoitus_polku = "../../train/train-"
testi_polku = "../../test/t10k-"

def lataa_kuvat(polku):
    with open(os.path.join(os.path.dirname(__file__),(polku +"images.idx3-ubyte")), 'rb') as kuvat:
        magic, kuvat_koko = struct.unpack(">II", kuvat.read(8))
        rivien_maara, sarakkeiden_maara = struct.unpack(">II", kuvat.read(8))
        kuva_array = np.fromfile(kuvat, dtype=np.dtype(np.uint8).newbyteorder('>'))
        kuva_array = kuva_array.reshape((kuvat_koko, rivien_maara, sarakkeiden_maara))

    return kuva_array

def lataa_nimikkeet(polku):
    with open(os.path.join(os.path.dirname(__file__),(polku+ "labels.idx1-ubyte")), 'rb') as nimikkeet:
        magic, nimikkeet_koko = struct.unpack(">II", nimikkeet.read(8))
        nimike_array = np.fromfile(nimikkeet, dtype=np.dtype(np.uint8).newbyteorder('>'))
        nimike_array = nimike_array.reshape((nimikkeet_koko,))

    return nimike_array



def raportti(oikein, n, i, tulokset, ruudut, aika, piirrin):
    print(">"*20)
    piirrin.ruudut_konsolissa(ruudut)
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
    luokiteltava = pistejoukko(lataa_kuvat(testi_polku)[0])
                                                                        #ladataan csv tiedostoista harjoitusdata runtime listoihin.
    harjoitusdata = csvk.lue_tiedostosta("kordinaatit.csv")             #harjoitusdata on 2D lista jossa jokainen rivi on [y,x] kordinaattipari (lista) 
    harjoitusnimikkeet = csvk.lue_tiedostosta("nimikkeet.csv")          #nimikkeet ovat normaali lista
    harjoitusruudut = csvk.lue_tiedostosta("ruudut.csv")                #ruudut ovat 3D lista jossa jokainen rivi sisältää 28x28 2D listan
                                                                        #tämä 2D listan kohdassa [y][x] on kyseisen pisteen pixelin totuusarvo(boolean)


    testinimikkeet = lataa_nimikkeet(testi_polku)                       #ladataan testinimikkeet normaali lista

    tulokset = []
    oikein = 0
    luok_num = random.randint(0,9999)                                   #valitaan indeksi testikuvalle. Kuvien arvioinnin absoluuttinen nopeus vaihtelee
                                                                        #eri kuvien välillä joten on hyvä testata eri kuvilla.


    for i in range(luok_num,luok_num+10):                                #arvioidaan yksi kuva, rakenne helposti muutettavissa tarkkuuden arviointiin.
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


