""" Excerises 2 """
import numpy as np
a = np.array( [5, 4, 9, 2, 0, 4, 7, 2])
#Part a 
EndChar = a[-1]
print(EndChar)
#Part b
MidChars = a[1:6]
print(MidChars) #the second to sixth characters
PenUltChar = a[:-2] 
print(PenUltChar) #all but the last character
ExtraChar = a[::2]
print(ExtraChar) #prints every other character
