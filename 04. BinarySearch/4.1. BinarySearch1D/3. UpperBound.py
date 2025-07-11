def upperBound(arr: list[int], x: int, n: int) -> int:
    # Write your code here.
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > x:
            n = mid
            high = mid - 1
        else:
            low = mid + 1
    return n

# https://www.codingninjas.com/studio/problems/implement-upper-bound_8165383