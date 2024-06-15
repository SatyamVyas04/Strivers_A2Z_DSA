import heapq


class Solution:
    def replaceWithRank(self, N, arr):
        heap = arr[:]
        heapq.heapify(heap)

        sorted_arr = []
        while heap:
            sorted_arr.append(heapq.heappop(heap))

        rank = {}
        current_rank = 1
        for num in sorted_arr:
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1

        ans = [rank[num] for num in arr]

        return ans

# Link: https://www.geeksforgeeks.org/problems/replace-elements-by-its-rank-in-the-array/1