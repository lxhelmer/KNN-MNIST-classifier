import os
#import matplotlib.pyplot as plt
import numpy as np
import struct
from data.pointsetmaker import pistejoukko 
from data.csvKaantaja import kirjoita_tiedostoon, lue_tiedostosta
with open(os.path.join(os.path.dirname(__file__),("../../test/t10k-images.idx3-ubyte")), 'rb') as kuvat:
    magic, kuvat_koko = struct.unpack(">II", kuvat.read(8))
    rivien_maara, sarakkeiden_maara = struct.unpack(">II", kuvat.read(8))
    kuva_array = np.fromfile(kuvat, dtype=np.dtype(np.uint8).newbyteorder('>'))
    kuva_array = kuva_array.reshape((kuvat_koko, rivien_maara, sarakkeiden_maara))

with open(os.path.join(os.path.dirname(__file__),("../../test/t10k-labels.idx1-ubyte")), 'rb') as nimikkeet:
    magic, nimikkeet_koko = struct.unpack(">II", nimikkeet.read(8))
    nimike_array = np.fromfile(nimikkeet, dtype=np.dtype(np.uint8).newbyteorder('>'))
    nimike_array = nimike_array.reshape((nimikkeet_koko,))


#for i in range(1, 2):
#    for y in range(0,rivien_maara):
#        print(data[i,y,:])

#plt.imshow(data[1,:,:], cmap='gray')
#plt.show()


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

def piirra_pistejoukko(pistejoukot):
    for numero in pistejoukot:
        y = int(numero[0][0])
        x = int(numero[0][1])
        print(y,x)
        numerostr = "." * (28 * int(numero[0][0]))
        numerostr = numerostr + "." * int(numero[0][1])
        numerostr = numerostr + "#"
        for piste in range(1,len(numero)):
            #print(numero[piste])
            numerostr = numerostr + "." * (int(numero[piste][0]) - int(numero[piste-1][0]))
            numerostr = numerostr + "." * (int(numero[piste][1]) - int(numero[piste-1][1]))
            numerostr = numerostr + "#"
        numerostr = numerostr + "." * (784-len(numerostr))
        for char in range(0,784):
            print(" " + numerostr[char] + " ",end="")
            if char%28 == 0:
                print("\n")
#        print (pistejoukot)

    
for i in range(0, 1):
    showinconsole(kuva_array[i,:,:])
    print(i)
    kirjoita_tiedostoon(np.asarray(pistejoukko(kuva_array[i,:,:])),"rajat.csv")
    kirjoita_tiedostoon([nimike_array[i]],"nimikkeet.csv")

piirra_pistejoukko(lue_tiedostosta("rajat.csv"))
    




