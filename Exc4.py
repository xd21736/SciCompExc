"""Excersise 4"""
import numpy as np
import math
import matplotlib.pyplot as plt 

t = np.linspace(0,5,500)
y = np.multiply(np.multiply(t,t),np.exp(-2*t))

fig, ax = plt.subplots()
ax.plot(t,y)
ax.set_ylabel("y(t)")
ax.set_xlabel("t")
ax.set_title("Graph for excersise 4")

MaxIndex = np.argmax(y)
MaxY = y[MaxIndex]
MaxT = t[MaxIndex]
plt.plot(MaxT,MaxY,'ro', label='Max value of y(t)')
plt.legend()
plt.show()

