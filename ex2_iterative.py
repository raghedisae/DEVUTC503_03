# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:45:26 2019

@author: raghed
"""


def rendreMonnaie(x):
    x=int(x)
    monnaie = [1000,5000]
    change = []
    y = x
    while monnaie:
        divideBy = int(monnaie.pop())
        change.append(int(x/divideBy))
        x = x%divideBy
    print ("rendre de",y,"est:",change)


 

#test
rendreMonnaie(5000)
rendreMonnaie(8000)
rendreMonnaie(7000)
rendreMonnaie(9000)

