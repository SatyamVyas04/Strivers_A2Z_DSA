class Solution:
    def rearrangeArray(self, nums: [int]) -> [int]:
        p, n = 0, 1
        ans = [0]*len(nums)
        for i in nums:
            if i>0:
                ans[p] = i
                p+=2
            else:
                ans[n] = i
                n+=2
        return ans

# Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/