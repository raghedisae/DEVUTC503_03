# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:45:26 2019

@author: raghed
"""


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


#test
print(rendreMonnaie([5000,1000],7000))
print(rendreMonnaie([5000,1000],8000))
print(rendreMonnaie([5000,1000],5000))
print(rendreMonnaie([5000,1000],9000))
