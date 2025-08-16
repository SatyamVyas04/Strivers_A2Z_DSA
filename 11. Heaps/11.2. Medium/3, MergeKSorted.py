import heapq


class Solution:
    def mergeKArrays(self, arr, K):
        # Heap of lists of all elements
        heap = []
        ans = []

        for array in arr:
            for num in array:
                heapq.heappush(heap, num)

        for _ in range(len(heap)):
            ans.append(heapq.heappop(heap))

        return ans

# Link: https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
