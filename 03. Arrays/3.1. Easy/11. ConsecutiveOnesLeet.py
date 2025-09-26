class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        streak, maxstreak = 0, 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                streak += 1
            else:
                maxstreak = max(maxstreak, streak)
                streak = 0
        maxstreak = max(maxstreak, streak)
        return maxstreak

# Link: https://leetcode.com/problems/max-consecutive-ones/
