class Solution:
    def minEatingSpeed(self, v: list[int], h: int) -> int:
        from math import ceil
        low = 1
        high = max(v)
        ans = float("inf")
        while low <= high:
            mid = (low + high) // 2
            totalhrs = 0
            for i in v:
                totalhrs += ceil(i/mid)
            if totalhrs <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return int(ans)

# Link: https://leetcode.com/problems/koko-eating-bananas/