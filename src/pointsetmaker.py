import numpy as np

def pistejoukko(mnistkuva):
    ret_pistejoukko = []
    for y in range(0, 28):
        for x in range(0,28):
            if mnistkuva[y,x] != 0:
                ret_pistejoukko.append((y,x))


    return ret_pistejoukko
