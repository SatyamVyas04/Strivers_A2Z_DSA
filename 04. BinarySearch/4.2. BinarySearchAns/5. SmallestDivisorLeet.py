from math import ceil
class Solution:
    def smallestDivisor(self, nums: [int], threshold: int) -> int:
        low = 1
        high = max(nums)
        n = len(nums)
        while low <= high:
            mid = (low + high) // 2
            total = 0
            for i in range(n):
                total += ceil(nums[i]/mid)
            if total <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
# Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/