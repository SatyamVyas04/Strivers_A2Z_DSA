class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.ans = []
        self.arr = []

        def helper(index, nums, n):
            if index == n:
                self.ans.append(self.arr[:])
                return
            self.arr.append(nums[index])
            helper(index+1, nums, n)
            self.arr.pop()
            helper(index+1, nums, n)
        helper(0, nums, len(nums))
        return self.ans

# Link: https://leetcode.com/problems/subsets/
