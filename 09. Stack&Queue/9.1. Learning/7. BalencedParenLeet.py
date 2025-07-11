class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or i != d[stack.pop()]:
                return False

        return len(stack) == 0

# Link: https://leetcode.com/problems/valid-parentheses/