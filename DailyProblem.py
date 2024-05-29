from math import log2


class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        num = int(s, 2)
        while s != 1:
            curr_power = log2(num)
            if int(curr_power) == curr_power:
                ans += int(curr_power)
                break
            elif num & 1:
                num += 1
            else:
                num //= 2
            ans += 1
        return ans


sol = Solution()
print(sol.numSteps("1101"))
