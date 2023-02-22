class Piirrin:
    def __init__(self):
        pass

    def mnist_konsolissa(mnist_numero):     #Mnist pikseliesityksen (2D lista arvoja 0-255) näyttäminen konsolissa. Toimii vian numpy arraylle.
        print("")
        print("".join(["---"*28]))
        for y in range(0,28):
            print("\n")
            for x in range(0,28):
                if number[y,x] != 0:
                    print(" # ",end="")
                else:
                    print(" . ",end="")

    def piirra_pistejoukko(pistejoukko):    #Yhden numeron kuvaa kuvaavan kordinaatti joukon esittäminen konsolissa
        xs = []
        ys = []
        for piste in pistejoukko:
            ys.append(piste[0])
            xs.append(piste[1])
        plt.scatter(xs,ys)
        plt.ylim(28,0)
        plt.xlim(0,28)
        plt.show()

    def ruudut_konsolissa(ruudut):          #2D totuus taulun esittäminen graafisesti konsolissa
        for y in range(0,28):
            print("\n")
            for x in range(0,28):
                if ruudut[y][x] == True:
                    print(" # ", end="")
                else:
                    print(" . ", end="")
        print("")
