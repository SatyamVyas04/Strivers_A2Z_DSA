from typing import *
from collections import Counter


def countFrequency(n: int, m: int, edges: List[List[int]]):
    ans = [0]*n
    c = dict(Counter(edges))
    for i in range(n):
        if i+1 in c:
            ans[i] = c[i+1]
    return ans

# Link: https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446
