from typing import *


def getLongestZeroSumSubarrayLength(arr: List[int]) -> int:
    # Write your code here.
    hashmap = {}
    s = 0
    maxlen = 0
    for i in range(len(arr)):
        curr = arr[i]
        s += curr
        if s == 0:
            maxlen = i+1

        rem = 0 - s
        if rem in hashmap.keys():
            maxlen = max(maxlen, i - hashmap[rem])

        if s in hashmap.keys():
            maxlen = max(maxlen, i - hashmap[s])  # Slight Change here
        else:
            hashmap[s] = i

    return maxlen

# Link: https://www.codingninjas.com/studio/problems/longest-subarray-with-zero-sum_6783450
