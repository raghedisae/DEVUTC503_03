# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:16:20 2019

@author: raghed
"""

my_list=[x**2 for x in range(10) if x%2==0]
print (my_list)

square = lambda x: x**2
double = lambda x: x + x
print(list(map(square, my_list)))
print(list(map(double, my_list)))


import functools
my_list = [1, 2, 3, 4, 5]
def add_it(x, y):
    return (x + y)
sum = functools.reduce(add_it, my_list)
print(sum)