class Solution:
    def checkValidString(self, s: str) -> bool:
        S = []
        for x in s:
            if x == "(" or x == "*":
                S.append(x)
            else:
                if len(S) > 0:
                    S.pop()
                else:
                    return False

        S = []
        for x in s[::-1]:
            if x == ")" or x == "*":
                S.append(x)
            else:
                if len(S) > 0:
                    S.pop()
                else:
                    return False
        return True

# Link: https://leetcode.com/problems/valid-parenthesis-string/description/
