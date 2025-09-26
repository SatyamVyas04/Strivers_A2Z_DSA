def longestSubarrayWithSumK(a: list[int], k: int) -> int:
    # Write your code here
    left, right = 0, 0
    n = len(a)
    maxlen = 0
    s = a[0]
    while right < n:
        while left <= right and s > k:
            s -= a[left]
            left += 1

        if s == k:
            maxlen = max(maxlen, right - left + 1)

        right += 1
        if right < n:
            s += a[right]

    return maxlen

# Link: https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399
