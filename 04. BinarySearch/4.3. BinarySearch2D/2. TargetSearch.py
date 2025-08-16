def search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 0


def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    for i in range(len(mat)):
        x = search(mat[i], target)
        if x == 1:
            return True
    return False

# Link: https://www.codingninjas.com/studio/problems/search-in-a-2d-matrix_980531
