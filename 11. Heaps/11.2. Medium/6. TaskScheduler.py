from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        c = Counter(tasks)
        maxheap = [-count for count in c.values()]
        heapq.heapify(maxheap)
        q = []
        time = 0
        while maxheap or q:
            time += 1
            if maxheap:
                popped_count = 1 + heapq.heappop(maxheap)
                if popped_count < 0:
                    q.append([popped_count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.pop(0)[0])
        return time
    
# Link: https://leetcode.com/problems/task-scheduler/