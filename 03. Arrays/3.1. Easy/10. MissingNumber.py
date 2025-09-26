class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor = 0
        for i in range(0, len(nums)):
            xor = xor ^ (i+1) ^ nums[i]
        return xor

    # Logic: a^b^b = a

# Link: https://leetcode.com/problems/missing-number/
