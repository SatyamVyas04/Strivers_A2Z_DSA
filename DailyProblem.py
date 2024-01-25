class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        nb, ns = len(text1), len(text2)
        dp = [[0 for _ in range(nb)] for _ in range(ns)]
        for row in range(ns):
            for col in range(nb):
                if text2[row] == text1[col]:
                    try:
                        dp[row][col] = 1 + dp[row-1][col-1]
                    except:
                        dp[row][col] = 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return dp[-1][-1]


sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))
