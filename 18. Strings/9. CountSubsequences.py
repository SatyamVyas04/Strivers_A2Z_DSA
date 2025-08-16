class Solution:
    def countPS(self, s):
        n = len(s)
        t = [[0] * n for _ in range(n)]
        for i in range(n):
            t[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    t[i][j] = 1 + t[i + 1][j] + t[i][j - 1]
                else:
                    t[i][j] = t[i + 1][j] + t[i][j-1] - t[i+1][j-1]
        return t[0][n-1]

# Link: https://www.geeksforgeeks.org/problems/count-palindromic-subsequences/1
