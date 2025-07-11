class Stack:
    def __init__(self, n: int):
        """
        Initialises a array that serves the purpose of storing data in it.
        """
        self.size = n
        self.topptr = -1
        self.stack = [0] * self.size

    def push(self, num: int):
        """
        Appends a number at the end of the array, at the (n-1)th index.
        in C and C++, using a constant space array, we manipulate the top pointer to move ahead.

        arr[++top] = num; 
        """
        if not self.isFull():
            self.topptr += 1
            self.stack[self.topptr] = num

    def pop(self) -> int:
        """
        Removes a number at the end of the array, at the (n-1)th index.
        in C and C++, using a constant space array, we manipulate the top pointer to move a place behind.

        top--; 
        """
        if not self.isEmpty():
            popped_val = self.stack[self.topptr]
            self.topptr -= 1
            return popped_val
        else:
            return -1

    def top(self) -> int:
        """
        Return the value stored at the last index or the (n-1)th index.
        """
        if not self.isEmpty():
            return self.stack[self.topptr]
        else:
            return -1

    def isEmpty(self) -> int:
        """
        Return whether or not the stack is empty or not.
        in C and C++, we can check for this condition by checking the top pointer.

        top == -1;
        """
        return self.topptr == -1

    def isFull(self) -> int:
        """
        Return whether or not the stack is full or not.
        in C and C++, we can check whether top pointer is equal to the size pointer or not

        top == size

        Here, in Python, a constant size array is taken, for this particular question
        """
        return self.topptr == self.size - 1


# Link: https://www.codingninjas.com/studio/problems/stack-implementation-using-array_3210209
