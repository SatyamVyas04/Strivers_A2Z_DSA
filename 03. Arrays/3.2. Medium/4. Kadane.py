def maxSubarraySum(arr, n):
    s, m = 0, 0

    for i in arr:
        s += i
        m = max(m, s)
        if s < 0:
            s = 0
    return m

# Link: https://www.codingninjas.com/studio/problems/maximum-subarray-sum_630526
