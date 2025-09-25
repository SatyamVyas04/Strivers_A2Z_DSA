from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        for i in range(1, len(triangle)):
            curr = triangle[i]
            n = len(curr)
            curr[0] += prev[0]
            curr[-1] += prev[-1]
            for j in range(1, n - 1):
                left_taken = curr[j] + prev[j - 1]
                right_taken = curr[j] + prev[j]
                curr[j] = min(left_taken, right_taken)
            prev = curr
        return min(prev)

# Link: https://leetcode.com/problems/triangle/
