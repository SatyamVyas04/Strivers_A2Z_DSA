class Solution:
    def InfixtoPostfix(self, exp):
        precedence = {"^": 3, "/": 2, "*": 2, "+": 1, "-": 1, "(": 0}
        opstack = []
        ans = ""

        for i in exp:
            if i in "^/*+-":
                while opstack and precedence[opstack[-1]] >= precedence[i]:
                    ans += opstack.pop()
                opstack.append(i)
            elif i == "(":
                opstack.append(i)
            elif i == ")":
                while opstack and opstack[-1] != "(":
                    ans += opstack.pop()
                opstack.pop()
            else:
                ans += i

        while opstack:
            ans += opstack.pop()

        return ans

# Link: https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1