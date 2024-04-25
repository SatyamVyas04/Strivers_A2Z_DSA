class Solution:
    def longestIdealString(self, arr: str, k: int) -> int:
        ans = 0
        n = len(arr)
        memo = {}

        def ideal(s: str) -> bool:
            for i in range(1, len(s)):
                if abs(ord(s[i]) - ord(s[i - 1])) > k:
                    return False
            return True

        def recur(s: str, ptr: int) -> None:
            nonlocal ans
            if s in memo:
                res = memo[s]
            else:
                res = ideal(s)
                memo[s] = res
            if res:
                ans = max(len(s), ans)
            if ptr < n:
                recur(s + arr[ptr], ptr + 1)
                recur(s, ptr + 1)

        recur("", 0)
        return ans

# Memory Limit Exceeded
# This is absolute Brute Force


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26
        for c in s:
            curr = ord(c) - ord('a')
            longest = 1
            for prev in range(26):
                if abs(prev - curr) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = longest
        return max(dp)


# DP Solution
# Works now :+1
