""" Excersise3 """
import numpy as np
#import math
A = np.array([[1,0,0,0],[1,-2,0,0],[0,1,-2,1],[0,0,0,1]])
b = np.array([0,1,1,2])
x = np.linalg.solve(A,b)
print(x)
print(A@x-b) #outputs 0. as its a floating point value