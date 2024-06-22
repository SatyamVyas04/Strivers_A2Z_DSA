class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_index = 0
        for idx, jump in enumerate(nums):
            if idx > max_index:
                return False
            max_index = max(max_index, idx + jump)
        return True


# Link: https://leetcode.com/problems/jump-game/submissions/1296661468/
