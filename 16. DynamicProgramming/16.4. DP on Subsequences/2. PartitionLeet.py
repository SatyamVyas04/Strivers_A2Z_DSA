class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        k = sum(nums)
        if k % 2 == 1:
            return False

        middle = k // 2
        # we just need to prove that we can reach the middle point
        # using some members of the array, because the rest will then
        # automatically be equal to the first half :) big brain

        dp = [[False for _ in range(middle + 1)] for _ in range(len(nums))]

        # middle 0 toh achieve kar lenge sab
        for i in range(len(nums)):
            dp[i][0] = True

        # agar first element is less than k, toh le sakta hu
        if nums[0] <= middle:
            dp[0][nums[0]] = True

        # ab agar middle tak we can make it, then sorted
        for index in range(1, len(nums)):
            for target in range(1, middle + 1):
                notTake = dp[index-1][target]
                take = False
                if nums[index] <= middle:
                    take = dp[index-1][target - nums[index]]
                dp[index][target] = take or notTake

        # for row in dp:
        #     print(row)
        #
        # Example: 3, 3, 3, 4, 5
        # [True, False, False, True, False, False, False, False, False, False]
        # [True, False, False, True, False, False, True , False, False, False]
        # [True, False, False, True, False, False, True , False, False, True ]
        # [True, False, False, True, True , False, True , True , False, True ]
        # [True, True , True , True, True , True , True , True , True , True ]

        return dp[len(nums) - 1][middle]

# Link: https://leetcode.com/problems/partition-equal-subset-sum/
