# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         size = len(cardPoints) - k
#         S = sum(cardPoints[size:])
#         ans = S
#         for i in range(0, k):
#             S += cardPoints[i]
#             S -= cardPoints[i+size]
#             ans = max(ans, S)
#         return ans


# My Solution
class Solution:
    def maxScore(self, nums: list[int], k: int) -> int:
        l = k
        r = len(nums)

        # Initial sum of the first k elements
        ans = sum(nums[:l])
        current_sum = ans

        for i in range(1, k + 1):
            current_sum = current_sum - nums[l - i] + nums[r - i]
            ans = max(ans, current_sum)

        return ans

# Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
