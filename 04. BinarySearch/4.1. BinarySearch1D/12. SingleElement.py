def singleNonDuplicate(arr):
    # Write your code here
    n = len(arr)
    if n == 1:
        return arr[0]

    low = 1
    high = n - 2

    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]

    while low <= high:
        mid = (low + high)//2
        if arr[mid-1] != arr[mid] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif arr[mid-1] == arr[mid] and mid % 2 == 0:  # odd even
            high = mid - 1
        elif arr[mid-1] == arr[mid] and mid % 2 == 1:  # even odd
            low = mid + 1
        elif arr[mid+1] == arr[mid] and mid % 2 == 0:  # even odd
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Link: https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654
