class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.md = {}
        self.s = []

    def get(self, key: int) -> int:
        if key in self.md:
            self.s.remove(key)
            self.s.append(key)
            return self.md[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.md:
            self.s.remove(key)
        self.md[key] = value
        self.s.append(key)
        if len(list(self.md.keys())) > self.capacity:
            k = self.s[0]
            del self.md[k]
            self.s.pop(0)


# Link: https://leetcode.com/problems/lru-cache/submissions/1280814571/
