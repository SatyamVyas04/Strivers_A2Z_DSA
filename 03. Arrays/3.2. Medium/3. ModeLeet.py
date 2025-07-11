class Solution:
    def majorityElement(self, nums: [int]) -> int:
        return sorted(nums)[len(nums)//2]

# Link: https://leetcode.com/problems/majority-element/