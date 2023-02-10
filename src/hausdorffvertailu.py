import math

def m_hausdorff_etaisyys(luokiteltava, harjoitus):
    return max(d_6(luokiteltava, harjoitus),d_6(harjoitus,luokiteltava))

def etaisyys_a_b(piste_a, piste_b):
    return abs(math.sqrt((piste_a[0]-piste_b[0])**2 + (piste_a[1]-piste_b[1])**2))

def etaisyys_a_B(piste_a, joukko_B):
    minimi = math.inf
    for piste_b in joukko_B:
        #print(piste_a)
        #print(piste_b)
        if etaisyys_a_b(piste_a, piste_b) < minimi:
            minimi = etaisyys_a_b(piste_a,piste_b)
    return minimi

def d_6(joukko_A, joukko_B):
    summa = 0
    for piste_a in joukko_A:
        summa += etaisyys_a_B(piste_a, joukko_B)
    
    return (1/len(joukko_A)) * summa

