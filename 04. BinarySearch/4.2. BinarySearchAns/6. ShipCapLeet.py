class Solution:
    def shipWithinDays(self, weights: [int], days: int) -> int:
        n = len(weights)
        low = max(weights)
        high = sum(weights)
        ans = sum(weights)

        while low<=high:
            mid = (low + high) // 2

            total = 0
            daystaken = 1
            for i in weights:
                total += i
                if total > mid:
                    daystaken += 1
                    total = i

            if daystaken <= days:
                high = mid - 1
            else:
                low = mid + 1 
                
        return low

# Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/