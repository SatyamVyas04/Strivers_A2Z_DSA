from typing import *

def missingK(vec: List[int], n: int, k: int) -> int:
    # Write your code here.
    n = len(vec)
    low = 0
    high = n-1        
    missing = 0
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - mid - 1
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    
    return high + k + 1

# Link: https://www.codingninjas.com/studio/problems/kth-missing-element_893215