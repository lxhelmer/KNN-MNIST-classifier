import os
import time
#import matplotlib.pyplot as plt
import numpy as np
import struct
import random
from data.pointsetmaker import pistejoukko, ruudut 
from data.csvKaantaja import kirjoita_tiedostoon, lue_tiedostosta
from kPienimmat import k_pienimmat

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


def showinconsole(number):
    print("")
    print("".join(["---"*28]))
    for y in range(0,28):
        print("\n")
        for x in range(0,28):
            if number[y,x] != 0:
                print(" # ",end="")
            else:
                print(" . ",end="")

def piirra_pistejoukko(pistejoukko):
    xs = []
    ys = []
    for piste in pistejoukko:
        ys.append(piste[0])
        xs.append(piste[1])
    plt.scatter(xs,ys)
    plt.ylim(28,0)
    plt.xlim(0,28)
    plt.show()

def piirra_ruudut(ruudut):
    print(ruudut)
    for y in range(0,28):
        print("\n")
        for x in range(0,28):
            if ruudut[y][x] == True:
                print(" # ", end="")
            else:
                print(" . ", end="")




#for i in range(0, 60000):
#    kuvat = lataa_kuvat(harjoitus_polku)
#    nimikkeet = lataa_nimikkeet(harjoitus_polku)
#    showinconsole(kuvat[0,:,:])
#    print(i)
#    kirjoita_tiedostoon(pistejoukko(kuvat[i,:,:]),"kordinaatit.csv")
#    kirjoita_tiedostoon(ruudut(kuvat[i,:,:]), "ruudut.csv")
#    kirjoita_tiedostoon([nimikkeet[i]],"nimikkeet.csv")



#piirra_pistejoukko(lue_tiedostosta("rajat.csv")[0])
    

k = 11
luokiteltava = pistejoukko(lataa_kuvat(testi_polku)[0])
harjoitusdata = lue_tiedostosta("kordinaatit.csv")
harjoitusnimikkeet = lue_tiedostosta("nimikkeet.csv")
harjoitusruudut = lue_tiedostosta("ruudut.csv")
testinimikkeet = lataa_nimikkeet(testi_polku)


#print(harjoitusnimikkeet)
#showinconsole(lataa_kuvat(testi_polku)[0])
#arvio = k_pienimmat(k, luokiteltava, harjoitusdata, harjoitusnimikkeet)
#print(arvio)

tulokset = []
oikein = 0
luok_num = random.randint(0,9999)
#piirra_ruudut(harjoitusruudut[luok_num])
#piirra_pistejoukko(pistejoukko(lataa_kuvat(testi_polku)[luok_num]))
#print(pistejoukko(lataa_kuvat(testi_polku)[luok_num]))
#print(testinimikkeet[20])
for i in range(luok_num,luok_num+1):
    luokiteltava_mnist = lataa_kuvat(testi_polku)[i]
    luokiteltava = pistejoukko(luokiteltava_mnist)
    print("alkaa")
    alku_aika = time.time()

    arvio = k_pienimmat(k, luokiteltava, harjoitusdata, harjoitusnimikkeet, harjoitusruudut, ruudut(luokiteltava_mnist))
    
    loppu_aika = time.time()

    print("loppui, aika: " + str(loppu_aika - alku_aika))
    tulokset.append([arvio,testinimikkeet[i]])
    
    if arvio == testinimikkeet[i]:
        oikein += 1


    print("-"*20)
    #print("Tarkkuus: " + str((i+1)/oikein))
    print(i+1)
    print("-"*20)

for res in tulokset:
    print("Arvioitu luku: " + str(res[0]) + " | Todellinen luku: " + str(res[1]),end="")
    if res[0] == res[1]:
        print(" |  SAMA!!!")
    else:
        print("")
