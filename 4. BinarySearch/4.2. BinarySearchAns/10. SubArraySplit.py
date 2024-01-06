def subarrcheck(arr, cap):
    s = 1
    total = 0
    for i in arr:
        if total + i <= cap:
            total += i
        else:
            s += 1
            total = i
    return s


def largestSubarraySumMinimized(a: [int], k: int) -> int:
    # Write Your Code Here
    if k > len(a):
        return -1
    low = max(a)
    high = sum(a)
    while low <= high:
        mid = (low + high)//2
        check = subarrcheck(a, mid)
        if check > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Link: https://www.codingninjas.com/studio/problems/largest-subarray-sum-minimized_7461751