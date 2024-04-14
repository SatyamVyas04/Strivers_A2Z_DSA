from collections import deque


class MyStack:
    def __init__(self):
        self.first = deque()
        self.second = deque()

    def push(self, x: int) -> None:
        self.second.append(x)
        while self.first:
            self.second.append(self.first.popleft())
        self.first, self.second = self.second, self.first

    def pop(self) -> int:
        if self.empty():
            return -1
        return self.first.popleft()

    def top(self) -> int:
        if self.empty():
            return -1
        return self.first[0]

    def empty(self) -> bool:
        if len(self.first) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
