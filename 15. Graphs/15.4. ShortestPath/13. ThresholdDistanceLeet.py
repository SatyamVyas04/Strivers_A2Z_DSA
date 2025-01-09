from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for src, dest, wgt in edges:
            graph[src].append((dest, wgt))
            graph[dest].append((src, wgt))

        def dijkstra(start):
            distances = [float('inf')] * n
            distances[start] = 0
            pq = [(0, start)]

            while pq:
                dist, node = heapq.heappop(pq)

                if dist > distances[node]:
                    continue

                for neighbor, weight in graph[node]:
                    new_dist = dist + weight
                    if new_dist < distances[neighbor] and new_dist <= distanceThreshold:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

            return sum(1 for d in distances if d <= distanceThreshold) - 1

        min_reachable = float('inf')
        result = -1

        for city in range(n):
            reachable = dijkstra(city)
            if reachable <= min_reachable:
                min_reachable = reachable
                result = city

        return result

# Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
