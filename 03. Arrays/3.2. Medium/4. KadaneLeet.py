class Solution:
    def maxSubArray(self, arr: [int]) -> int:
        s, m = 0, arr[0]
        for i in arr:
            s += i
            m = max(s, m)
            if s < 0:
                s = 0
        return m

# Link: https://leetcode.com/problems/maximum-subarray/
