# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:58:53 2024

@author: farka
"""
## Excersise 1##
import numpy
import scipy
import matplotlib
from math import pi

def Leibniz(n):
    Estimate = 0
    for i in range(n):
        Estimate += 8/((4*i+1)*(4*i+3))
    return abs(pi-Estimate)   
n=100
while Leibniz(n)>=1e-7:
    n *= 5
print(n)