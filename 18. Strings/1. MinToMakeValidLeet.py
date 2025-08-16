class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        ops = 0
        adds = 0
        for ch in string:
            if ch == "(":
                ops += 1
            else:
                if ops > 0:
                    ops -= 1
                else:
                    adds += 1
        return adds + ops

# Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
