class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robber(nums[1:]), self.robber(nums[:-1]))

    def robber(self, nums: list[int]) -> int:
        prev2, prev1 = 0, nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            pick = curr
            if i > 1:
                pick += prev2
            not_pick = prev1
            curr = max(pick, not_pick)
            prev2, prev1 = prev1, curr
        return prev1

# Link: https://leetcode.com/problems/house-robber-ii/
