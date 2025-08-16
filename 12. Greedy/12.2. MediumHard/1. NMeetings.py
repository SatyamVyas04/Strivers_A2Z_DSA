import heapq


class Solution:
    def maximumMeetings(self, n, start, end):
        minheap = []
        for i in range(n):
            heapq.heappush(minheap, (end[i], start[i], i))

        ans = 0
        last_end = -1
        while minheap:
            curr_end, curr_start, _ = heapq.heappop(minheap)
            if curr_start > last_end:
                ans += 1
                last_end = curr_end

        return ans

# Link: https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
