class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row = 0
        col = m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return 1
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return 0

# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
