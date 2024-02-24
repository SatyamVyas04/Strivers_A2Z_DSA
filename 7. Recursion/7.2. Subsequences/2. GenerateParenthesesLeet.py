class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def gen(op, close, stack, res):
            if op == close == n:
                res.append(stack)
                return

            if op < n:
                stack += "("
                gen(op+1, close, stack, res)
                stack = stack[:-1]

            if close < op:
                stack += ")"
                gen(op, close+1, stack, res)
                stack = stack[:-1]

        gen(0, 0, "", res)
        return res

# Link: https://leetcode.com/problems/generate-parentheses/
