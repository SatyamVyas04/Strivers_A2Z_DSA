class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        ans = 0
        for i in s:
            if i == "(":
                depth += 1
                if depth > 0:
                    ans = max(depth, ans)
            elif i == ")":
                depth -= 1
        return ans

# Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/