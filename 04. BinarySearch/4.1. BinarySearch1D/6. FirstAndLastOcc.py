from os import *
from sys import *
from collections import *
from math import *


def firstAndLastPosition(arr, n, k):
    low = 0
    high = n-1
    a, b = -1, n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= k:
            a = mid
            high = mid - 1
        else:
            low = mid + 1

    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > k:
            b = mid
            high = mid - 1
        else:
            low = mid + 1

    if arr[a] != k:
        return (-1, -1)
    return (a, b-1)

# Link: https://www.codingninjas.com/studio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549
