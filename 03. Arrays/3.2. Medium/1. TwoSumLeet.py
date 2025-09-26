class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

# Link: https://leetcode.com/problems/two-sum/
