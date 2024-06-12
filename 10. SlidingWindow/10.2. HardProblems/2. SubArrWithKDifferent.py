from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        lfar = 0
        lnear = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while len(count) > k:
                count[nums[lnear]] -= 1
                if count[nums[lnear]] == 0:
                    count.pop(nums[lnear])
                lnear += 1
                lfar = lnear
            while count[nums[lnear]] > 1:
                count[nums[lnear]] -= 1
                lnear += 1
            if len(count) == k:
                res += lnear - lfar + 1
        return res

# Link: https://leetcode.com/problems/subarrays-with-k-different-integers/