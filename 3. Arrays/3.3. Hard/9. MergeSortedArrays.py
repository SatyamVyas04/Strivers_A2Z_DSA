from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    # Write your code here.
    n, m = len(a), len(b)
    left, right = n-1, 0
    while left >= 0 and right < m:
        if a[left] > b[right]:
            a[left], b[right] = b[right], a[left]
            left -= 1
            right += 1
        else:
            break
    a.sort()
    b.sort()

# Link: https://www.codingninjas.com/studio/problems/merge-two-sorted-arrays-without-extra-space_6898839