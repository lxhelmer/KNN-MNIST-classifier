import numpy as np

def pistejoukko(mnistkuva):
    kordinaatit = np.where(mnistkuva != 0)
    ret_pistejoukko = np.hstack((kordinaatit[0][:,np.newaxis],kordinaatit[1][:,np.newaxis]))
    return ret_pistejoukko

def ruudut(mnistkuva):
    ret_ruudut = mnistkuva > 0
    return ret_ruudut
