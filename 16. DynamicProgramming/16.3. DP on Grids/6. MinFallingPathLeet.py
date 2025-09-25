from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        if n == 1:
            total = 0
            for r in range(m):
                total += matrix[r][0]
            return total

        prev = matrix[0]
        for i in range(1, m):
            curr = matrix[i]
            curr[0] += min(prev[0], prev[1])
            curr[-1] += min(prev[-1], prev[-2])
            for j in range(1, n - 1):
                curr[j] += min(prev[j - 1], prev[j], prev[j + 1])
            prev = curr
        return min(prev)

# Link: https://leetcode.com/problems/minimum-falling-path-sum/description/
