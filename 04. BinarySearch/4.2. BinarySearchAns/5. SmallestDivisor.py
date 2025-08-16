from os import *
from sys import *
from collections import *
from math import *


def smallestDivisor(arr: [int], limit: int) -> int:
    # Write your code here.
    low = 1
    high = max(arr)
    ans = float("inf")
    while low <= high:
        mid = (low + high) // 2
        currsum = 0
        for i in arr:
            currsum += ceil(i/mid)
        if currsum <= limit:
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    return ans

# Link: https://www.codingninjas.com/studio/problems/smallest-divisor-with-the-given-limit_1755882
