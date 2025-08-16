class Solution:
    def __init__(self):
        self.cap = 0
        self.curr = 0
        self.cache = []
        self.faults = 0

    def pageFaults(self, n, c, pages):
        # N -> number of pages
        # C -> cache size
        # Pages -> array of pages

        self.cap = c
        for i in range(n):
            page = pages[i]
            if not self.get(page):
                self.faults += 1
                self.put(page)
            else:
                continue

        return self.faults

    def get(self, key: int) -> int:
        try:
            index = self.cache.index(key)
            page = self.cache.pop(index)
            self.cache.append(page)
            return 1
        except ValueError:
            return 0

    def put(self, key: int) -> None:
        if self.curr < self.cap:
            self.cache.append(key)
            self.curr += 1
        else:
            self.cache.pop(0)
            self.cache.append(key)


# Link: https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1
