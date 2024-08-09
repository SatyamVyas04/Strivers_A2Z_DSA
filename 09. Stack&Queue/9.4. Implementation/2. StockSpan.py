class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            top = self.stack.pop()
            span += top[-1]
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Link: https://leetcode.com/problems/online-stock-span/description/
