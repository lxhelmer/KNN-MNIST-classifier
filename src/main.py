import os
#import matplotlib.pyplot as plt
import numpy as np
import struct
from pointsetmaker import pistejoukko 
with open(os.path.join(os.path.dirname(__file__),("../../train/train-images.idx3-ubyte")), 'rb') as f:
    magic, koko = struct.unpack(">II", f.read(8))
    rivien_maara, sarakkeiden_maara = struct.unpack(">II", f.read(8))
    data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
    data = data.reshape((koko, rivien_maara, sarakkeiden_maara))


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


    
for i in range(0, 10):
    showinconsole(data[i,:,:])
    print("")
    pistejoukko = np.asarray(pistejoukko(data[i,:,:]))
    print(np.asarray(pistejoukko(data[i,:,:])))


#print(np.empty([1,1]))


