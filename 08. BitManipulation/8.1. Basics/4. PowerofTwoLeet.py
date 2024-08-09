class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0

# Link: https://leetcode.com/problems/power-of-two/description/
