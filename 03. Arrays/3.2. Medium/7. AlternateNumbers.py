from typing import *


def alternateNumbers(a: List[int]) -> List[int]:
    # Write your code here.
    ans = [0] * len(a)
    p, n = 0, 1
    for i in a:
        if i > 0:
            ans[p] = i
            p += 2
        else:
            ans[n] = i
            n += 2
    return ans

# Link: https://codingninjas.com/studio/problems/alternate-numbers_6783445
