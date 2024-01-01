from os import *
from sys import *
from collections import *
from math import *

def getFloorAndCeil(arr, n, x):
    # Write your code here.
    low = 0
    high = n-1
    upper = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            upper = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    low = 0
    high = n-1
    lower = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            lower = arr[mid]
            low = mid + 1
        else:
            high = mid - 1

    return (lower, upper)

# Link: https://www.codingninjas.com/studio/problems/ceiling-in-a-sorted-array_1825401