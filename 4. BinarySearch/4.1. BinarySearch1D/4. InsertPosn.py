def searchInsert(arr: [int], x: int) -> int:
    # Write your code here.
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1 
        else:
            low = mid + 1
            
    return ans

# Link: https://www.codingninjas.com/studio/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813