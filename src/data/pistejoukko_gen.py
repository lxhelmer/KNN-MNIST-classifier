import numpy as np

#Yksinkertainen työkaluluokka joka muuttaa numpy array muodossa
#olevan mnist tiedon tehokkaasti haluttuun esitysmuotoon, joko
#kordinaattijoukoksi tai y,x totuustauluksi

def pistejoukko(mnistkuva):
    kordinaatit = np.where(mnistkuva != 0)
    ret_pistejoukko = np.hstack((kordinaatit[0][:,np.newaxis],kordinaatit[1][:,np.newaxis]))
    return ret_pistejoukko

def ruudut(mnistkuva):
    ret_ruudut = mnistkuva > 0
    return ret_ruudut
