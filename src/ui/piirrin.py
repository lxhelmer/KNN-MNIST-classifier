import matplotlib.pyplot as plt

# pylint: disable = invalid-name

class Piirrin:
    def __init__(self):
        pass

    #Mnist pikseliesityksen (2D lista arvoja 0-255) näyttäminen konsolissa.
    #Toimii vain numpy arraylle.
    def mnist_konsolissa(self,mnist_numero):
        print("")
        print("".join(["---"*28]))
        for y in range(0,28):
            print("\n")
            for x in range(0,28):
                if mnist_numero[y,x] != 0:
                    print(" # ",end="")
                else:
                    print(" . ",end="")
        print("loppui")

    #Yhden numeron kuvaa kuvaavan kordinaatti joukon esittäminen konsolissa
    def piirra_pistejoukko(self,pistejoukko):
        xs = []
        ys = []
        for piste in pistejoukko:
            ys.append(piste[0])
            xs.append(piste[1])
        plt.scatter(xs,ys)
        plt.ylim(28,0)
        plt.xlim(0,28)
        plt.show()

    #2D totuustaulun esittäminen graafisesti konsolissa
    def ruudut_konsolissa(self,ruudut):
        for y in range(0,28):
            print("\n")
            for x in range(0,28):
                if ruudut[y][x] is True:
                    print(" # ", end="")
                else:
                    print(" . ", end="")
        print("")
