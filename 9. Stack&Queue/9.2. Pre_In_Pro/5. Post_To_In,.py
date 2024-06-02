class Solution:
    def postToInfix(self, postfix):
        stack = []
        for i in postfix:
            if i in "+-*/^":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append("(" + op2 + i + op1 + ")")
            else:
                stack.append(i)
        return stack.pop()

# Link: https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1