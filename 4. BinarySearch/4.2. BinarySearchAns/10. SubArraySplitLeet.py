class Solution:
    def splitArray(self, nums: [int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            s = 1
            t = 0
            for i in nums:
                if t + i <= mid:
                    t += i
                else:
                    t = i
                    s += 1
            if s > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
    
# Link: https://leetcode.com/problems/split-array-largest-sum/