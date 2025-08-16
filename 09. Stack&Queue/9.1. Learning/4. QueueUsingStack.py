class Queue:
    def __init__(self) -> None:
        # Initialize your data structure here.
        self.first = []
        self.second = []

    def enQueue(self, val: int) -> None:
        # Implement the enqueue() function.
        while self.first:
            self.second.append(self.first.pop())
        self.first.append(val)
        while self.second:
            self.first.append(self.second.pop())

    def deQueue(self) -> int:
        # Implement the dequeue() function.
        if self.isEmpty():
            return -1
        return self.first.pop()

    def peek(self) -> int:
        # Implement the peek() function here.
        if self.isEmpty():
            return -1
        return self.first[-1]

    def isEmpty(self) -> bool:
        # Implement the isEmpty() function here.
        return self.first == []

# Link: https://www.naukri.com/code360/problems/day-25-:-queue-using-stack_799482
