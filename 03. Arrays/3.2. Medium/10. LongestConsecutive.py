from typing import *

def longestSuccessiveElements(arr : List[int]) -> int:
    # Write your code here.
    arr.sort()
    maxl = 1
    curl = 1
    for i in range(0, len(arr)-1):
        if arr[i+1] == arr[i]: 
            continue

        elif arr[i+1] - arr[i] == 1:
            curl += 1
        else:
            maxl = max(maxl, curl)
            curl = 1
    
    return max(curl, maxl)

# Link: https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740