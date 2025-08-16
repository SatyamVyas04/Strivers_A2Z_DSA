class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        last = float("-inf")
        ans = 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start >= last:
                last = end
            else:
                ans += 1
        return ans

# Link: https://leetcode.com/problems/non-overlapping-intervals/
