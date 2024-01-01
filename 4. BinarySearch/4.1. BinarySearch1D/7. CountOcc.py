def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    ans = firstAndLastPosition(arr, n, x)
    return ans
    

def firstAndLastPosition(arr, n, k):
    low = 0
    high = n-1
    a, b = -1, n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= k:
            a = mid
            high = mid - 1
        else:
            low = mid + 1
    
    low = 0
    high = n-1
    while low <= high: 
        mid = (low + high)//2
        if arr[mid] > k:
            b = mid
            high = mid - 1
        else:
            low = mid + 1
    
    if arr[a] != k:
        return 0    # Changed
    return b-a      # Changed

# Link: https://www.codingninjas.com/studio/problems/occurrence-of-x-in-a-sorted-array_630456