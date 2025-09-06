class Solution:
    def frogJump(self, heights, k):
        n = len(heights)
        dp = [0] * n
        dp[0] = 0

        for i in range(1, n):
            minimum = float("inf")
            for j in range(1, min(k, i) + 1):
                jump = dp[i-j] + abs(heights[i] - heights[i-j])
                minimum = min(minimum, jump)
            dp[i] = minimum

        return dp[n-1]

# Link: https://takeuforward.org/plus/dsa/problems/frog-jump-with-k-distances
