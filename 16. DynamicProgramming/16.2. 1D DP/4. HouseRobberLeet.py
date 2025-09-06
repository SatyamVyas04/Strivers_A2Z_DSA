# 1. Recursion: from the element i, if we pick it, we can go back to i - 2, else, if we leave the current i element, we can go to the i - 1 behind it and choose it. This was we can generate all subsequences. We find overlapping subproblems here
# 2. Base Case: i == 0 is where we add arr[0], i == -1 if where we add 0
# 3. Memoization: let's create a dp array, to store dp[i] which represents the max sum upto 0...i in the array
# 4. Tabulate: use dp array for this pick / not pick problem
# 5. Space Complexity: we just need 3 variables, for curr, prev1, prev2, to determine our choice.

class Solution:
    def rob(self, nums: list[int]) -> int:
        # dp = [-1] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     pick = nums[i]
        #     if i > 1:
        #         pick += dp[i-2]
        #     not_pick = dp[i-1]
        #     dp[i] = max(pick, not_pick)
        # return dp[-1]

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

# Link: https://leetcode.com/problems/house-robber/
