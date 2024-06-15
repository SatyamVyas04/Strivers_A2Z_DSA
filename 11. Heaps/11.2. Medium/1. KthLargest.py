import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return -1 * res

# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
