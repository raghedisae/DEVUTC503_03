# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:01:15 2019

@author: raghed
"""
monnaie=(5000,1000)
m= 8000

change=[m//x if m-x>x else (m-10000)//x for x in monnaie]
print(change)
