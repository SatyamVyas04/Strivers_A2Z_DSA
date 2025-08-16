def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    k = k % len(arr)
    arr[:] = arr[k:] + arr[:k]
    return arr

# Link: https://www.codingninjas.com/studio/problems/rotate-array_1230543
