# class MedianFinder:
#     def __init__(self):
#         self.arr = []
#         self.n = 0

#     def addNum(self, num: int) -> None:
#         self.arr.insert(bisect.bisect(self.arr, num), num)
#         self.n += 1

#     def findMedian(self) -> float:
#         if self.n & 1:
#             return self.arr[self.n//2]
#         return (self.arr[self.n//2] + self.arr[self.n//2 - 1])/2

import heapq


class MedianFinder:
    def __init__(self):
        self.smallarr = []  # maxheap
        self.largearr = []  # minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallarr, -num)

        # Sort
        while self.smallarr and self.largearr and (-self.smallarr[0] > self.largearr[0]):
            value = -1 * heapq.heappop(self.smallarr)
            heapq.heappush(self.largearr, value)

        # Length Check
        if len(self.smallarr) > len(self.largearr) + 1:
            value = -1 * heapq.heappop(self.smallarr)
            heapq.heappush(self.largearr, value)
        if len(self.largearr) > len(self.smallarr) + 1:
            value = -1 * heapq.heappop(self.largearr)
            heapq.heappush(self.smallarr, value)

    def findMedian(self) -> float:
        if len(self.smallarr) > len(self.largearr):
            return -self.smallarr[0]
        elif len(self.smallarr) < len(self.largearr):
            return self.largearr[0]
        else:
            return (-self.smallarr[0] + self.largearr[0])/2

# Link: https://leetcode.com/problems/find-median-from-data-stream/submissions/1298859103/
