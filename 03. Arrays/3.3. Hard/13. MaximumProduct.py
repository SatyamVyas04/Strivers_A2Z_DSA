from typing import *


def subarrayWithMaxProduct(arr: List[int]) -> int:
    # Write your code here.
    ans = float('-inf')
    n = arr.__len__()
    prefix, suffix = 0, 0
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= arr[i]
        suffix *= arr[n-i-1]

        ans = max(ans, max(prefix, suffix))

    return ans

# Link: https://www.codingninjas.com/studio/problems/subarray-with-maximum-product_6890008
