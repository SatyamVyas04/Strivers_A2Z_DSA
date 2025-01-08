from collections import defaultdict, deque
import math


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int):
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u - 1].append((v - 1, w))

        hops = [math.inf] * n
        hops[k-1] = 0
        q = deque([(k-1)])
        while q:
            node = q.popleft()
            for nei, wei in adj[node]:
                if hops[node] + wei < hops[nei]:
                    hops[nei] = hops[node] + wei
                    q.append(nei)

        ans = max(hops)
        if ans == math.inf:
            return -1
        return ans

# Link: https://leetcode.com/problems/network-delay-time/submissions/1501563366/
