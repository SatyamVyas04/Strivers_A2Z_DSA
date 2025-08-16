class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        n0, n1 = 0, 1
        for i in range(2, n+1):
            curr = n0+n1
            n0, n1 = n1, curr
        return curr

# Link: https://leetcode.com/problems/fibonacci-number/
