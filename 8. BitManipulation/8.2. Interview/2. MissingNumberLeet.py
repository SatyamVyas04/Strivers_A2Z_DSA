from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        c = dict(Counter(nums))
        for i in c.keys():
            if c[i] == 1:
                return i
        return -1

# Link:https://leetcode.com/problems/single-number/
