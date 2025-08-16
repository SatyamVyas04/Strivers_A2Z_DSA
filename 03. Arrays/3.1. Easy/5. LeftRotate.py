from sys import *
from collections import *
from math import *


def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    first_element = arr.pop(0)
    arr.append(first_element)
    return arr

# Link: https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278
