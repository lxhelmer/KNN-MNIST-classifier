import numpy as np

def pistejoukko(mnistkuva):
    YX = np.where(mnistkuva != 0)
    ret_pistejoukko = np.hstack((YX[0][:,np.newaxis],YX[1][:,np.newaxis]))
    return ret_pistejoukko;

def ruudut(mnistkuva):
    ret_ruudut = mnistkuva > 0
    return ret_ruudut
