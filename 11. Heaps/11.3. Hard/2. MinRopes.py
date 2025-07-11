import heapq


class Solution:
    def minCost(self, arr, n):
        heapq.heapify(arr)
        ans = 0
        while len(arr) >= 2:
            first, second = heapq.heappop(arr), heapq.heappop(arr)
            ans += first + second
            heapq.heappush(arr, first + second)
        return ans


sol = Solution()
print(sol.minCost([4, 3, 2, 6], 4))

# Link: https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1