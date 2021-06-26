import numpy as np

def vecteurStochastique  (n:[]) :
    if (sum(n) == 1):
        return True
    return False 

def matriceStochastique (m):
    for i in m:
        if (vecteurStochastique(i)):
            continue
        else:
            return False
    return True        
        

def matricePower(m, power) : 
    mArray = np.array(m)
    matrix = np.matrix(mArray)
    return matrix**power       

n = [1,0]
m = [1,1]

A = [
        [0.2,0.6,0.2], 
        [1,0,0],
        [0.1,0.5,0.4]   
    ]

B = [
        [1,2,3], 
        [0,1,0],
        [0,0,1]
    ]
    
print('N = ',n)
print('M = ',m)
print('A = ',A)
print('B = ',B)

print('N est un vecteur Stochastique :',vecteurStochastique(n))
print('M est un vecteur Stochastique :',vecteurStochastique(m))
print('A est une matrice Stochastique :',matriceStochastique(A))
print('B est une matrice Stochastique :',matriceStochastique(B))

p = 0
print('Saisir un nombre entier p (puissance)\n')
try : 
    p = int(input())
    print('A*',p,' = ',matricePower(A,p))
except : 
    print('svp saisir un nombre entier\n')