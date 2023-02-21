import numpy as np
def reuna(mnistkuva,y,x):
    if (y == 0 or y == 27 or x == 0 or x == 27):
        return True
    
    elif mnistkuva[y-1,x-1] == 0 or mnistkuva[y-1,x] == 0 or mnistkuva[y-1,x+1] == 0:
        return True
    elif mnistkuva[y,x-1] == 0 or mnistkuva[y,x+1]== 0:
        return True
    elif mnistkuva[y+1,x-1] == 0 or mnistkuva[y+1,x] == 0 or mnistkuva[y+1,x+1] == 0:
        return True
    else:
        return False

def pistejoukko(mnistkuva):
    ret_pistejoukko = []
    for y in range(0, 28):
        for x in range(0,28):
            if mnistkuva[y,x] != 0: 
                    ret_pistejoukko.append([y,x])

    return ret_pistejoukko

def ruudut(mnistkuva):
    ret_ruudut = []
    for y in range(0,28):
        rivi = []
        for x in range(0,28):
            if mnistkuva[y,x] != 0:
                rivi.append(True)
            else:
                rivi.append(False)
        ret_ruudut.append(rivi)
    return ret_ruudut
