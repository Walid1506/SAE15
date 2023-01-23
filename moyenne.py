from math import sqrt

def moyenneL (liste):
    moyenne = 0
    for i in liste :
        moyenne +=1
    moyenne = moyenne/len(liste)
    return moyenne


def ecarType(liste):
    moyenne = 0
    ecartT = 0
    
    for i in liste :
        moyenne +=1
        moyenne = moyenne/len(liste)
        
    for x in liste :
        ecartT += (x - moyenne)**2
        ecartT /= len(liste)
        ecartT = sqrt(ecartT)
    return ecartT