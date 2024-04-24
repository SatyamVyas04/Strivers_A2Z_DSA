class MinStack:
    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        currmin = self.getMin()
        if val < currmin:
            self.arr.append((val, val))
        else:
            self.arr.append((val, currmin))

    def pop(self) -> None:
        self.arr.pop()[0]

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        if self.arr:
            return self.arr[-1][1]
        else:
            # Relaxed type since there's no better way to represent inf in int
            return float("inf")
