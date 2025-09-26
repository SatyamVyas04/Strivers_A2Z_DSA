class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = m*n - 1
        while low <= high:
            mid = (low+high)//2
            i, j = divmod(mid, m)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

# Link: https://leetcode.com/problems/search-a-2d-matrix/
