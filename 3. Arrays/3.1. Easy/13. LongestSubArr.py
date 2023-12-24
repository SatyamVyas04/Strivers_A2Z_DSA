def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    n = len(a)
    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        Sum += a[i]
        if Sum == k:
            maxLen = max(maxLen, i + 1)
        rem = Sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

# Link: https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399