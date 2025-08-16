from typing import *


def superiorElements(a: List[int]) -> List[int]:
    # Write your code here.
    s = [a[-1]]
    maxi = a[-1]
    for i in range(len(a)-2, -1, -1):
        if a[i] > maxi:
            s.append(a[i])
            maxi = max(maxi, a[i])
    return s

# Link: https://www.codingninjas.com/studio/problems/superior-elements_6783446
