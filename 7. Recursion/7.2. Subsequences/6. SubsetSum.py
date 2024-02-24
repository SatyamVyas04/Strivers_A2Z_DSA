from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    def helper(n, k, a, total, idx) -> bool:
        if total == k:
            return True
        if idx >= n:
            return False

        c1 = helper(n, k, a, total+a[idx], idx + 1)
        if c1:
            return True
        c2 = helper(n, k, a, total, idx + 1)
        if c2:
            return True
        return False
        
    return helper(n, k, a, 0, 0)

# Link: https://www.codingninjas.com/studio/problems/subset-sum_630213