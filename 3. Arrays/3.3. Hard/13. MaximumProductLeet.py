class Solution:
    def maxProduct(self, nums: [int]) -> int:
        ans = float('-inf')
        n = nums.__len__()
        prefix, suffix = 0, 0
        for i in range(n):
            if suffix == 0:
                suffix = 1
            if prefix == 0:
                prefix = 1
            
            prefix *= nums[i]
            suffix *= nums[n-i-1]

            ans = max(ans, max(prefix, suffix))

        return ans
    
# Link: https://leetcode.com/problems/maximum-product-subarray/