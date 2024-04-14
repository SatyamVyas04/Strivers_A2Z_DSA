from collections import deque
from inspect import ismemberdescriptor


class Stack:
    def __init__(self):
        # Define the data members.
        self.first = deque()
        self.second = deque()

    def getSize(self) -> int:
        # Implement the getSize() function.
        return len(self.first)

    def isEmpty(self) -> bool:
        # Implement the isEmpty() function.
        return self.getSize() == 0

    def push(self, element: int) -> None:
        # Implement the push() function.
        self.second.append(element)
        while self.first:
            self.second.append(self.first.popleft())
        self.first, self.second = self.second, self.first

    def pop(self) -> int:
        # Implement the pop() function.
        if not self.isEmpty():
            return self.first.popleft()
        return -1

    def top(self) -> int:
        # Implement the top() function.
        if not self.isEmpty():
            return self.first[0]
        return -1

# Link: https://www.naukri.com/code360/problems/stack-using-queue_795152
