def findKRotation(arr : list[int]) -> int:
    # Write your code here.
    n = len(arr)
    if n == 1:
        return 0
    
    low = 0
    high = n-1
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            if arr[low] < arr[ans]:
                ans = low
            low = mid + 1
        else:
            if arr[mid] < arr[ans]:
                ans = mid
            high = mid - 1
    return ans

# Link: https://www.codingninjas.com/studio/problems/rotation_7449070