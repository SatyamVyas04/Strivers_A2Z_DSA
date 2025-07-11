from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        heap = [(-c, k) for c, k in zip(hashmap.values(), hashmap.keys())]
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

# Link: https://leetcode.com/problems/top-k-frequent-elements/
