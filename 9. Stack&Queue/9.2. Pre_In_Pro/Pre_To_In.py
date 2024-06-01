class Solution:
    def preToInfix(self, pre_exp):
        stack = []
        i = len(pre_exp) - 1
        while i >= 0:
            if pre_exp[i] not in "^-+/*()":
                stack.append(pre_exp[i])
                i -= 1
            else:
                string = "(" + stack.pop() + pre_exp[i] + stack.pop() + ")"
                stack.append(string)
                i -= 1
        return stack.pop()
