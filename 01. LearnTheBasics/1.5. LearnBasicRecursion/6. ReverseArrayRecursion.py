from typing import *


def reverseArray(n: int, nums: List[int]) -> List[int]:
    l2 = []
    if n == 1 or n == 0:
        return nums

    def recur(n, nums):
        if n == 0:
            return
        l2.append(nums.pop())
        recur(n-1, nums)
    recur(n, nums)
    return l2

# Link: https://www.codingninjas.com/studio/problems/reverse-an-array_8365444
