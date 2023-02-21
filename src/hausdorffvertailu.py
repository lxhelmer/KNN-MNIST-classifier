import math

def m_hausdorff_etaisyys(luokiteltava, harjoitus, ruudut_luokiteltava, ruudut_harjoitus):
    return max(d_6(luokiteltava, harjoitus, ruudut_luokiteltava),d_6(harjoitus,luokiteltava, ruudut_harjoitus))

def minimi_a_b(piste_a, piste_b):
    return (piste_a[0]-piste_b[0])**2 + (piste_a[1]-piste_b[1])**2

def etaisyys_a_B(piste_a, joukko_B, ruudut_B, juuri):
    minimi = math.inf
    aY = piste_a[0]
    aX = piste_a[1]
    
    lahimmat = ["0,0", #0
                "-1,0","0,1","1,0","0,-1", #1
                "-1,-1","-1,1","1,1","1,-1", #2
                "0,2","2,0","0,-2","-2,0", #4
                "-2,-1","-2,1","-1,2","1,2","2,1","

    if ruudut_B[aY][aX] == True:
        return 0

    for xy in [-1,1]:
        if aX + xy <= 27 and aX + xy >= 0:
            if ruudut_B[aX+xy][aY] == True:
                return 1
        if aY + xy <= 27 and aY + xy >= 0:
            if ruudut_B[aX][aY+xy] == True:
                return 1
    for xy in [-2
    for x in [-1,1]:
        for y in [-1,1]:
            if piste_a[0]+x <= 27 and piste_a[1]+y <= 27 and piste_a[0]+x >= 0 and piste_a[1] + y >= 0:
                if ruudut_B[piste_a[0]+x][piste_a[1]+y] == True:
                        return juuri

    for piste_b in joukko_B:
        arvo = minimi_a_b(piste_a, piste_b)
        if arvo < minimi:
            if arvo == 4:
                return 2
            minimi = arvo

    return math.sqrt(minimi)

def d_6(joukko_A, joukko_B,ruudut_B):
    summa = 0
    kahden_juuri = math.sqrt(2)

    for piste_a in joukko_A:
        summa += etaisyys_a_B(piste_a, joukko_B,ruudut_B, kahden_juuri)
    
    return (1/len(joukko_A)) * summa

