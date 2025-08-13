# 1. Recursion: n breaks to n-1 and n-2. During n-1 phase, n-2 soln is also calculated. This seems to be an overlapping problem.
# 2. Base case: n equal to 1, generates 1 answer, n equal to 2 generates 2
# 3. Memoize: dp[n] can be created, where dp[i] denotes the number of ways in which we can climb upto ith stair
# 4. Tabulation: use dp[] calls
# 5. Space: Will see later

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        if n > 1:
            dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
# Link: https://leetcode.com/problems/climbing-stairs/