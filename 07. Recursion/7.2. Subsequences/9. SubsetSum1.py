from sys import *
from collections import *
from math import *
from typing import List


def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    sumarr = []

    def helper(arr, idx, n, ds):
        if idx == n:
            sumarr.append(sum(ds))
            return

        ds.append(arr[idx])
        helper(arr, idx + 1, n, ds)
        ds.pop()
        helper(arr, idx + 1, n, ds)
    helper(num, 0, len(num), [])
    return sorted(sumarr)

# Link: https://www.codingninjas.com/studio/problems/subset-sum_3843086