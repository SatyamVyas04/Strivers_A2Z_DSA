# Implement class for minStack.
class minStack:
    # Constructor
    def __init__(self):
        # Write your code here.
        self.Stack = []  # (curr, min)
        self.Min = []  # Min

    # Function to add another element equal to num at the top of stack.
    def push(self, num: int) -> None:
        # Write your code here.
        currmin = self.getMin()
        if num < currmin or currmin < 0:
            self.Stack.append(num)
            self.Min.append(num)
        else:
            self.Stack.append(num)
            self.Min.append(currmin)

    # Function to remove the top element of the stack.
    def pop(self) -> int:
        # Write your code here.
        if self.Stack:
            self.Min.pop()
            return self.Stack.pop()
        return -1

    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self) -> int:
        # Write your code here.
        if self.Stack:
            return self.Stack[-1]
        return -1

    # Function to return min element of stack if it is present. Otherwise return -1.
    def getMin(self) -> int:
        # Write your code here.
        if self.Stack:
            return self.Min[-1]
        return -1

# Link: https://leetcode.com/problems/min-stack/
