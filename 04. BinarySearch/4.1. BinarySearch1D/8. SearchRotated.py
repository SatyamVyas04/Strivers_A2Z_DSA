def search(arr, n, k):
    # Write your code here
    low = 0
    high = n - 1
    ans = 0
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == k:
            return mid
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
    return -1

# Link: https://www.codingninjas.com/studio/problems/search-in-rotated-sorted-array_1082554
