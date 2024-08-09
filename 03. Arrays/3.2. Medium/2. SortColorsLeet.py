class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, len(nums)-1
        while one <= two:
            i = nums[one]
            if i == 1:
                one += 1
            elif i == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            else:
                nums[two], nums[one] = nums[one], nums[two]
                two -= 1
                
# Link: https://leetcode.com/problems/sort-colors/