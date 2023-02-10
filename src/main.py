import os
import matplotlib.pyplot as plt
import numpy as np
import struct
from data.pointsetmaker import pistejoukko 
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
    plt.show()


###
    
#for i in range(0,60000):
#    kuvat = lataa_kuvat(harjoitus_polku)
#    nimikkeet = lataa_nimikkeet(harjoitus_polku)
#    showinconsole(kuvat[0,:,:])
#    print(i)
#    kirjoita_tiedostoon(pistejoukko(kuvat[i,:,:]),"rajat.csv")
#    kirjoita_tiedostoon([nimikkeet[i]],"nimikkeet.csv")



#piirra_pistejoukko(lue_tiedostosta("rajat.csv")[0])
    

k = 5
luokiteltava = pistejoukko(lataa_kuvat(testi_polku)[0])
harjoitusdata = lue_tiedostosta("rajat.csv")
harjoitusnimikkeet = lue_tiedostosta("nimikkeet.csv")
testinimikkeet = lataa_nimikkeet(testi_polku)

print(k)
#print(luokiteltava)
#print(harjoitusdata)
#print(harjoitusnimikkeet)
#piirra_pistejoukko(luokiteltava)
#arvio = k_pienimmat(k, luokiteltava, harjoitusdata, harjoitusnimikkeet)
#print(arvio)

tulokset = []

for i in range(0,10):
    luokiteltava = pistejoukko(lataa_kuvat(testi_polku)[i]) 
    arvio = k_pienimmat(k, luokiteltava, harjoitusdata, harjoitusnimikkeet)
    tulokset.append([arvio,testinimikkeet[i]])

    print("-"*20)

    print(i+1)

for res in tulokset:
    print("Arvioitu luku: " + str(res[0]) + " | Todellinen luku: " + str(res[1]),end="")
    if res[0] == res[1]:
        print(" |  SAMA!!!")
    else:
        print("")
