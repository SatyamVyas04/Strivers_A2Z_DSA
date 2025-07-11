class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        num = set(nums)
        ans = 0
        for i in num:
            if i-1 in num:
                continue
            else:
                l = 1
                while i+1 in num:
                    l+=1
                    i+=1
            ans = max(ans, l)
        return ans
                
# Link: https://leetcode.com/problems/longest-consecutive-sequence/description/