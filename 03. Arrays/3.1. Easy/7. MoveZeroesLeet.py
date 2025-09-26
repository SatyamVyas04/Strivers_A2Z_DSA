class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
                n -= 1
            i += 1

# Link: https://leetcode.com/problems/move-zeroes/
