from collections import deque


class Solution:
    def minimumMultiplications(self, arr, start, end):
        if start == end:
            return 0
        mod = 100_000
        q = deque([(start, 0)])
        dist = [float('inf')] * mod
        dist[start] = 0

        while q:
            node, steps = q.popleft()

            for num in arr:
                next_node = (num * node) % mod

                if steps + 1 < dist[next_node]:
                    dist[next_node] = steps + 1
                    if next_node == end:
                        return steps + 1
                    q.append((next_node, steps + 1))

        return -1

# Link: https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
