class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = int("-" + str(abs(x))[::-1])
        if ans > 2**31-1 or ans < -2**31:
            return 0
        else:
            return ans

# Link: https://leetcode.com/problems/reverse-integer/
