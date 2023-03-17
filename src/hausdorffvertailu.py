import math
import numpy as np
from scipy.spatial.distance import cdist

# pylint: disable=C0103

class HausdorffVertailu:
    def __init__(self):
        pass

    def m_hausdorff_etaisyys(self, luokiteltava, harjoitus, ruudut_luokiteltava, ruudut_harjoitus):
        luokiteltava_harjoitus = self.d_6(luokiteltava, harjoitus, ruudut_harjoitus)
        harjoitus_luokiteltava = self.d_6(harjoitus,luokiteltava, ruudut_luokiteltava)

        return max(luokiteltava_harjoitus ,harjoitus_luokiteltava) #vertaillaan molempiin suuntiin

    #Koska koodia käytetään jokaisen luokittelun kohdalla polempiin suuntiin
    #Luokiteltava-Harjoitus, siirryin tässä kohdassa vähemmän kuvaaviin mutta loogisesti yhdenmukaisiin
    #muuttuja nimiin. Muuttujat sekä funktiot myös vastaavat lähdemateriaalin kaavoja mikä helpottaa koodin
    #ymmärtämistä.
    def etaisyys_a_B(self, piste_a, joukko_B, ruudut_B):
        minimi = 1600
        aY = piste_a[0]
        aX = piste_a[1]

        if ruudut_B[aY][aX] == True:
            return 0

        kordinaatit = [
                [1,0],[-1,0],[0,1],[0,-1], #etäisyys 1
                [1,1],[1,-1],[-1,1],[-1,-1],    #etäisyys sqrt 2
                [2,0],[-2,0],[0,2],[0,-2],  #etäisyys 2
                [2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2],    #etäisyys sqrt 5
                [2,2],[2,-2],[-2,2],[-2,-2],    #etäisyys sqrt(5)
                [3,0],[-3,0],[0,3],[0,-3], #etäisyys 3
                [3,1],[3,-1],[-3,1],[-3,-1],[1,3],[1,-3],[-1,3],[-1,-3], #etäisyys sqrt(10)
                [3,2],[3,-2],[-3,2],[-3,-2],[2,3],[2,-3],[-2,3],[-2,-3] #etäisyys sqrt(13)
                ]
        etaisyydet = {
                (1,0) : 1,
                (0,1) : 1,
                (1,1) : math.sqrt(2),
                (2,0) : 2,
                (0,2) : 2,
                (2,1) : math.sqrt(5),
                (1,2) : math.sqrt(5),
                (2,2) : math.sqrt(8),
                (3,0) : 3,
                (0,3) : 3,
                (3,1) : math.sqrt(10),
                (1,3) : math.sqrt(10),
                (3,2) : math.sqrt(13),
                (2,3) : math.sqrt(13)

                }
        #Käydään kordinaattien mukaisia ruutuja läpi totuustauluesityksestä. 
        #Järjestys on kasvava joten pisteen löytyessä voidaan kordinaatteja vastaava etäisyys
        #hakea etaisyydet dictistä ja palauttaa sillä sen tiedetään olevan pienin.
        for kordinaatti in kordinaatit:
            if  aY+kordinaatti[0] >= 0 and aY+kordinaatti[0] <= 27 and \
                aX+kordinaatti[1] >= 0 and aX+kordinaatti[1] <= 27:
                if ruudut_B[aY+kordinaatti[0]][aX+kordinaatti[1]] == True:
                    return etaisyydet[(abs(kordinaatti[0]),abs(kordinaatti[1]))]


        for piste_b in joukko_B:
            arvo = (piste_a[0]-piste_b[0])**2 + (piste_a[1]-piste_b[1])**2
            
            #Koska kaikki tätä pienemmät arvon on läpikäyty voidaan tällä tuloksella pysäyttää etsiminen.
            if arvo == 18:
                return math.sqrt(18)

            if arvo < minimi:
                minimi = arvo


        return math.sqrt(minimi)
        #return np.min(cdist(np.array([piste_a]), joukko_B))
        #nopea vaihtoehto (a-B) minimi etäisyyden laskemiselle
        #tosin tätä käyttäess tulee listojen olla numpy array muodossa
        #eikä etäisyyksien määrää ollut tehokasta karsio numpy arrayn
        #hitaamman lookup toiminnon takia.

    def d_6(self, joukko_A, joukko_B,ruudut_B):

        summa = 0
        for piste_a in joukko_A:
            summa += self.etaisyys_a_B(piste_a, joukko_B,ruudut_B)

        return summa/len(joukko_A)
