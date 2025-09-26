class Solution:
    def check(self, nums: list[int]) -> bool:
        return sum(nums[i] < nums[i-1] for i in range(0, len(nums))) <= 1

# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
