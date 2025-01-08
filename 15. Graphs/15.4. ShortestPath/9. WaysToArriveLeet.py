import math
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d:
                    continue  # Skip if `d` is not updated to latest version!
                for v, time in graph[u]:
                    if dist[v] > d + time:
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + time:
                        ways[v] = (ways[v] + ways[u]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)

# Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
