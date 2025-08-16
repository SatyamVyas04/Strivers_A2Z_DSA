from typing import *
from collections import Counter


def getSingleElement(arr: List[int]) -> int:
    # Write your code here.
    c = dict(Counter(arr))
    for i in c.keys():
        if c[i] == 1:
            return i

# Link: https://www.codingninjas.com/studio/problems/find-the-single-element_6680465
