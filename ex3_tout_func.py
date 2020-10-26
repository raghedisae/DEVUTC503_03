# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:45:26 2019

@author: raghed
"""
"""finctionnel Tous"""

def rendreMonnaie(r,x):
    x=int(x)
    monnaie = r
    monnaie.sort()
    change = []
    
    while monnaie:
        divideBy = int(monnaie.pop())
        change.append(int(x/divideBy))
        x = x%divideBy
    return change


def toutRendreMonnaie(r,x):
    x=int(x)
    tout=[]
    r.sort()
   
    while r:
        monnai=r.copy()
        tout.append(rendreMonnaie(monnai,x))
        r.pop()
    return tout
    


#test


print(toutRendreMonnaie([5000,1000],8000))
print(toutRendreMonnaie([9000,5000,1000],9000))
#toutRendreMonnaie([5000,1000],8000)
#toutRendreMonnaie([5000,1000],5000)
#toutRendreMonnaie([5000,1000],9000)