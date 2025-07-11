class Solution:
    def postToPre(self, post_exp):
        stack = []

        # Iterate through each character in the postfix expression
        for char in post_exp:
            if char not in "^/*+-":
                # If the character is an operand, push it to the stack
                stack.append(char)
            else:
                # If the character is an operator, pop two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()
                # Form the prefix expression by combining the operands and operator
                prefix = char + operand1 + operand2
                # Push the resulting prefix expression back to the stack
                stack.append(prefix)

        # The final prefix expression is the only element left in the stack
        return stack[-1]

# Link: https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1
