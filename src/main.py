import time
import numpy as np
import random
from lataaja import lataa_kuvat, lataa_nimikkeet
from data.pistejoukko_gen import pistejoukko, ruudut
from hausdorffvertailu import HausdorffVertailu
from klahimmat import KLahimmat
from ui.piirrin import Piirrin

HARJOITUS_POLKU = "../../train/train-"
TESTI_POLKU = "../../test/t10k-"
PIIRRIN = Piirrin()
HAUSDORFF = HausdorffVertailu()
KNN = KLahimmat(HAUSDORFF)


def raportti(oikein, yhteensa, tulokset,luok_ruudut, aika):
    print(">"*20)
    print("Arvio: ", str(yhteensa))
    print("Arvioon käytetty aika: " + str(aika))
    if oikein != 0:
        print("Kokonais tarkkuus: " + str(oikein/yhteensa))
    print("Arvio: " + str(tulokset[yhteensa-1][0]))
    print("Todellinen: " + str(tulokset[yhteensa-1][1]))
    print("<"*20)


def main():

    k = 21   # määritetään k arvo
    print("aloitetaan")
    harjoitus_mnist = lataa_kuvat(HARJOITUS_POLKU)
    print("harjoitus MNIST ladattu")

    #harjoitusdata on 2D Numpy array
    #jossa jokainen rivi on yksi kordinaattijoukko
    harjoitusdata = np.array(
            [pistejoukko(x) for x in harjoitus_mnist],
            dtype=object)
    print("Harjoitus pistejoukot luotu")

    #nimikkeet ovat 1D Numpy array
    harjoitusnimikkeet = lataa_nimikkeet(HARJOITUS_POLKU)
    print("Harjoitus nimikkeet ladattu")

    #ruudut ovat 3D-Numpy array
    #jossa jokainen rivi sisältää 28x28 2D Numpy arrayn
    harjoitusruudut = np.array(
            [ruudut(x) for x in harjoitus_mnist])
    print("Harjoitus ruudut luotu")

    testidata = lataa_kuvat(TESTI_POLKU)
    print("Testidata ladattu")

    testinimikkeet = lataa_nimikkeet(TESTI_POLKU)   #ladataan testinimikkeet normaali lista
    print("Testi nimikkeet ladattu")

    tulokset = []
    oikein = 0
    #luok_num = random.randint(0,9980)
    luok_num = 20
    harjoitusdata = harjoitusdata.tolist()
    harjoitusruudut = harjoitusruudut.tolist()

    for i in range(luok_num,luok_num+100):
        luokiteltava_mnist = testidata[i]
        luokiteltava = pistejoukko(luokiteltava_mnist).tolist() #luodaan pixelitoteutuksesta kordinaatti joukko
        luokiteltava_ruudut = ruudut(luokiteltava_mnist).tolist()


        print("alkaa")
        alku_aika = time.time()


        arvio = KNN.k_lahimmat(                                        #arvioidaan luokiteltavan kuvan nimike
                k,
                luokiteltava,
                harjoitusdata,
                harjoitusnimikkeet,
                harjoitusruudut,
                luokiteltava_ruudut
                )

        loppu_aika = time.time()


        tulokset.append([arvio,testinimikkeet[i]])

        if arvio == testinimikkeet[i]:
            oikein += 1


        raportti(oikein, i-luok_num+1, tulokset, luokiteltava_ruudut, loppu_aika-alku_aika)

    for res in tulokset:
        print("Arvioitu luku: " + str(res[0]) + " | Todellinen luku: " + str(res[1]),end="")
        if res[0] == res[1]:
            print(" |  SAMA!!!")
        else:
            print("")



if __name__ == "__main__":
    main()
