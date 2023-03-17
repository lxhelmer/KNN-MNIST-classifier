import time
import numpy as np
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
    PIIRRIN.ruudut_konsolissa(luok_ruudut)
    print("Arvio: ", str(yhteensa))
    print("Arvioon käytetty aika: " + str(aika))
    if oikein != 0:
        print("Kokonais tarkkuus: " + str(oikein/yhteensa))
    print("Arvio: " + str(tulokset[yhteensa-1][0]))
    print("Todellinen: " + str(tulokset[yhteensa-1][1]))
    print("<"*20)


def main():

    print("Ohjelma luokittelee haluttuja mnist t10k-testisetin kuvia käyttäen KNN metodia")
    print("ja muokattua hausdorff heuristiikkaa.")
    print("Luokittelu alkaa ilmoitetusta indeksistä ja päättyy halutun kuvamäärän")
    print("jälkeen tai kun viimeinen indeksin 9999 kuva on luokiteltu")

    while True:
        try:
            k = int(input("\nSyötä haluttu k: "))   # määritetään k arvo
            maara = int(input("\nSyötä luokiteltavien kuvien määrä (kesto n.40s per kuva) : "))
            luok_num = int(input("\nSyötä aloitus kuvan indeksi (0-9999): "))
            if k <= 0 or k > 60000 or maara <= 0 or maara > 9999 or luok_num < 0 or luok_num > 9999:
                print("syötä valideja lukuja")
                continue
            break
        except ValueError:
            print("Syötä vain numeroita!")
            continue

    loppu = luok_num+maara
    if luok_num+maara>10000:
        loppu = 10000

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
    harjoitusdata = harjoitusdata.tolist()
    harjoitusruudut = harjoitusruudut.tolist()
    kaikki = 0
    oikein = 0

    for i in range(luok_num,loppu):
        luokiteltava_mnist = testidata[i]
        luokiteltava = pistejoukko(luokiteltava_mnist).tolist() #luodaan pixelitoteutuksesta kordinaatti joukko
        luokiteltava_ruudut = ruudut(luokiteltava_mnist).tolist()

        print("alkaa")
        alku_aika = time.time()

        #arvioidaan luokiteltavan kuvan nimike
        arvio = KNN.k_lahimmat(
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
        kaikki += 1

        raportti(oikein, kaikki, tulokset, luokiteltava_ruudut, loppu_aika-alku_aika)

    #Näytetään lopuksi luokittelut kootusti
    for res in tulokset:
        print("Arvioitu luku: " + str(res[0]) + " | Todellinen luku: " + str(res[1]),end="")
        if res[0] == res[1]:
            print(" |  SAMA!!!")
        else:
            print("")



if __name__ == "__main__":
    main()
