class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        odd = 0
        cnt = 0
        l, r = 0, 0
        while r < n:
            if nums[r] % 2:
                odd += 1
                cnt = 0
            while odd == k:
                cnt += 1
                odd -= nums[l] & 1
                l += 1
            ans += cnt
            r += 1
        return ans
    
# Link: https://leetcode.com/problems/count-number-of-nice-subarrays/description/