"""Main"""
import math
import Solvers 
from scipy.optimize import root
def F(x):
    return math.cos(x)-x
def Fprime(x):
    return -math.sin(x)-1
NewtonRoot = Solvers.NextN(1,1e-10,F,Fprime)
print(NewtonRoot)

#Part C
SciRoot = root(F,0)
print(SciRoot)