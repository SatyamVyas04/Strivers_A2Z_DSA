class Solution:
    def rotate(self, A: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(i, m):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for i in range(n):
            A[i].reverse()

# Link: https://leetcode.com/problems/rotate-image/
