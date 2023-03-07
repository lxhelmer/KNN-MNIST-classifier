import math
import numpy as np
from scipy.spatial.distance import cdist

class HausdorffVertailu:
    def __init__(self):
        pass

    def m_hausdorff_etaisyys(self, luokiteltava, harjoitus, ruudut_luokiteltava, ruudut_harjoitus):
        AB = self.d_6(luokiteltava, harjoitus, ruudut_harjoitus)
        BA = self.d_6(harjoitus,luokiteltava, ruudut_luokiteltava)
        return max(AB,BA)

    def minimi_a_b(self, piste_a, piste_b):
        return (piste_a[0]-piste_b[0])**2 + (piste_a[1]-piste_b[1])**2

    def etaisyys_a_B(self, piste_a, joukko_B, ruudut_B, juuri):
        minimi = 1600
        aY = piste_a[0]
        aX = piste_a[1]
        

        if ruudut_B[aY][aX] == True:
            return 0
        
#        etaisyydet = [
#                [1,0],[-1,0],[0,1],[0,-1], #etäisyys 1
#                [1,1],[1,-1],[-1,1],[-1,-1],    #etäisyys sqrt 2
#                [2,0],[-2,0],[0,2],[0,-2],  #etäisyys 2
#                [2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2],    #etäisyys sqrt 5
#                [2,2],[2,-2],[-2,2],[-2,-2],    #etäisyys 3
#                [3,0],[-3,0],[0,3],[0,-3]   #etäisyys sqrt 10
#                ]
#        for et in [[1,0],[-1,0],[0,1],[0,-1]]:
#            if  aY+et[0] >= 0 and aY+et[0] <= 27 and \
#                aX+et[1] >= 0 and aX+et[1] <= 27:
#                if ruudut_B[aY+et[0]][aX+et[1]] == True:
#                    return 1
#            
#        for et in [[1,1],[1,-1],[-1,1],[-1,-1]]:
#            if  aY+et[0] >= 0 and aY+et[0] <= 27 and \
#                aX+et[1] >= 0 and aX+et[1] <= 27:
#                if ruudut_B[aY+et[0]][aX+et[1]] == True:
#                    return juuri
#
#        for et in [[2,0],[-2,0],[0,2],[0,-2]]:
#            if  aY+et[0] >= 0 and aY+et[0] <= 27 and \
#                aX+et[1] >= 0 and aX+et[1] <= 27:
#                if ruudut_B[aY+et[0]][aX+et[1]] == True:
#                    return 2
#
#        for et in [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]:
#            if  aY+et[0] >= 0 and aY+et[0] <= 27 and \
#                aX+et[1] >= 0 and aX+et[1] <= 27:
#                if ruudut_B[aY+et[0]][aX+et[1]] == True:
#                    return math.sqrt(5)
#
#        for et in [[2,2],[2,-2],[-2,2],[-2,-2]]:
#            if  aY+et[0] >= 0 and aY+et[0] <= 27 and \
#                aX+et[1] >= 0 and aX+et[1] <= 27:
#                if ruudut_B[aY+et[0]][aX+et[1]] == True:
#                    return math.sqrt(8)
#            
#        for et in [[3,0],[-3,0],[0,3],[0,-3]]:
#            if  aY+et[0] >= 0 and aY+et[0] <= 27 and \
#                aX+et[1] >= 0 and aX+et[1] <= 27:
#                if ruudut_B[aY+et[0]][aX+et[1]] == True:
#                    return 3
#
#        for piste_b in joukko_B:    
#            arvo = (piste_a[0]-piste_b[0])**2 + (piste_a[1]-piste_b[1])**2
#            if arvo == 10:
#                return math.sqrt(10)
#
#            if arvo < minimi:
#                minimi = arvo
        

        #return math.sqrt(minimi)
        return np.min(cdist(np.array([piste_a]), joukko_B))
    
    def d_6(self, joukko_A, joukko_B,ruudut_B):
        juuri = math.sqrt(2)
        summa = 0
        
        for piste_a in joukko_A:


            summa += self.etaisyys_a_B(piste_a, joukko_B,ruudut_B, juuri)
        
        return summa/len(joukko_A)

