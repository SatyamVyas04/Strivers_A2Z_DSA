def lowerBound(arr: list[int], n: int, x: int) -> int:
    # Write your code here
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= x:
            n = mid
            high = mid - 1
        else:
            low = mid + 1
    return n

# Link: https://www.codingninjas.com/studio/problems/lower-bound_8165382
