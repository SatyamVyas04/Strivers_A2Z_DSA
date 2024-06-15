import heapq


class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heapq.heapify(arr)
        for _ in range(k):
            res = heapq.heappop(arr)
        return res

# Link: https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1