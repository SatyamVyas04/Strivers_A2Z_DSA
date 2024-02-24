from collections import defaultdict


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        secrets = {0, firstPerson}
        time_map = {}

        for src, dst, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list[int])
            time_map[time][src].append(dst)
            time_map[time][dst].append(src)

        def dfs(src, adj):
            if src in visited:
                return
            visited.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        for time in sorted(time_map.keys()):
            visited = set()
            for src in time_map[time]:
                if src in secrets:
                    dfs(src, time_map[time])

        return list(secrets)


s = Solution()
print(s.findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))
