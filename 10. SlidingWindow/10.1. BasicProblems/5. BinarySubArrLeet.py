# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         hashmap = defaultdict(int)
#         hashmap[0] = 1 # Default Condition
#         count, presum = 0, 0
#         for i in nums:
#             presum += i
#             removal = presum - goal
#             count += hashmap[removal]
#             hashmap[presum] += 1
#         return count           

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        l, r = 0, 0
        temp, total = 0, 0
        ans = 0
        while r < len(nums):
            total += nums[r]
            if nums[r]:
                temp = 0
            while total > goal:
                total -= nums[l]
                l += 1
            while total == goal and l <= r:
                temp += 1
                total -= nums[l]
                l += 1
            r += 1
            ans += temp
        return ans
    
# Link: https://leetcode.com/problems/binary-subarrays-with-sum/