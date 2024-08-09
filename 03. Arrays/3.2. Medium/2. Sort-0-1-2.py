from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):
    zeroPos, onePos,twoPos = 0, 0, n - 1
    while onePos <= twoPos:
     	if arr[onePos] == 1:
            onePos += 1

        elif arr[onePos] == 0:
            arr[zeroPos], arr[onePos] = arr[onePos], arr[zeroPos]
            
            zeroPos += 1
            onePos += 1

        else:
            arr[onePos], arr[twoPos] = arr[twoPos], arr[onePos]
            
            twoPos -= 1

	# [1, 1, 1, 0, 2, 2, 1, 1, 2] <- Test on this

# Link: https://www.codingninjas.com/studio/problems/sort-an-array-of-0s-1s-and-2s_892977