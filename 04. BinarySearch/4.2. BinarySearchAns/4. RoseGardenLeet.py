class Solution:
    def minDays(self, bloomDay: [int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = (low + high) // 2
            bqt = 0
            ptr = 0
            for i in bloomDay:
                if i <= mid:
                    ptr += 1
                else:
                    bqt += ptr//k
                    ptr = 0
            bqt += ptr//k
            if bqt >= m:
                high = mid - 1
            else:
                low = mid + 1
        return low

# Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
