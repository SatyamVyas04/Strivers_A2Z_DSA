class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        maxLen = 0
        flip = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                flip += 1
            while flip > k:
                if nums[left] == 0:
                    flip -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen

# Link: https://leetcode.com/problems/max-consecutive-ones-iii/
