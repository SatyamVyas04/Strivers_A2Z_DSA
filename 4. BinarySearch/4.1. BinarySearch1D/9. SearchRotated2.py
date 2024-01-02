from typing import *

def searchInARotatedSortedArrayII(arr : List[int], k : int) -> bool:
    # Write your code here.
    low = 0
    high = len(arr) - 1
    ans = 0
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == k:
            return True
        elif arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
        elif arr[low] <= arr[mid]:
            if arr[low] <= k <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= k <= arr[high]:
                low = mid + 1    
            else:
                high = mid - 1
    return False

# Link: https://www.codingninjas.com/studio/problems/search-in-a-rotated-sorted-array-ii_7449547