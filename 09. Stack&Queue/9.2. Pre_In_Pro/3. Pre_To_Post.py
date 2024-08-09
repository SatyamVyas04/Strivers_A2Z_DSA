class Solution:
    def preToPost(self, pre_exp):
        stack = []
        # Reverse the prefix expression to process it from right to left
        pre_exp = pre_exp[::-1]

        # Iterate through each character in the reversed prefix expression
        for char in pre_exp:
            if char not in "^/*+-":
                # If the character is an operand, push it to the stack
                stack.append(char)
            else:
                # If the character is an operator, pop two operands from the stack
                operand1 = stack.pop()
                operand2 = stack.pop()
                # Form the postfix expression by combining the operands and operator
                postfix = operand1 + operand2 + char
                # Push the resulting postfix expression back to the stack
                stack.append(postfix)

        # The final postfix expression is the only element left in the stack
        return stack[-1]

# Link: https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1
