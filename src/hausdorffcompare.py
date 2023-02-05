import math

def m_hausdoff_etaisyys(luokiteltava, harjoitus):
    return max(d_6(luokiteltava, harjoitus),d_6(harjoitus,luokiteltava))

def etaisyys_a_B(piste_a, joukko_B)
    minimi = math.inf
    for piste_b in joukko_B:
        if abs(piste_a-piste_b) < minimi:
            minimi abs(piste_a-piste_b)
    return minimi

def d_6(joukko_A, joukko_B):
    summa = 0
    for piste_a in joukko a:
        summa += etaisyys_a_B(piste_a, joukkoB)
    
    return (1/len(joukko_A)) * summa
        

