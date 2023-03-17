import struct
import os
import numpy as np

#Yksinkertainen työkaluluokka jolla ladataan mnist data suorituksen aikaisiin
#muuttujiin.

def lataa_kuvat(polku):
    with open(os.path.join(os.path.dirname(__file__),(polku +"images.idx3-ubyte")), 'rb') \
    as kuvat:
        magic, kuvat_koko = struct.unpack(">II", kuvat.read(8))
        rivien_maara, sarakkeiden_maara = struct.unpack(">II", kuvat.read(8))
        kuva_array = np.fromfile(kuvat, dtype=np.dtype(np.uint8).newbyteorder('>'))
        kuva_array = kuva_array.reshape((kuvat_koko, rivien_maara, sarakkeiden_maara))
    return kuva_array

def lataa_nimikkeet(polku):
    with open(os.path.join(os.path.dirname(__file__),(polku+ "labels.idx1-ubyte")), 'rb') \
    as nimikkeet:
        magic, nimikkeet_koko = struct.unpack(">II", nimikkeet.read(8))
        nimike_array = np.fromfile(nimikkeet, dtype=np.dtype(np.uint8).newbyteorder('>'))
        nimike_array = nimike_array.reshape((nimikkeet_koko,))
    return nimike_array
