from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        children = len(g)

        gptr = 0
        for cookie in s:
            if gptr < children and cookie >= g[gptr]:
                gptr += 1

        return gptr

    def findContentChildrenDP(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        n = len(g)
        m = len(s)

        # dp[i][j] = max number of content children considering first i children and first j cookies
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                # Skip the j-th cookie
                dp[i][j] = dp[i][j-1]

                # Try to assign j-th cookie if it satisfies the i-th child greed
                if s[j-1] >= g[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

        return dp[n][m]

# Link: https://leetcode.com/problems/assign-cookies/description/
