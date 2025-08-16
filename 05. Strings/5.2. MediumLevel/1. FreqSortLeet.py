from collections import *


class Solution:
    def frequencySort(self, s: str) -> str:
        c = dict(Counter(s))
        arr = list(zip(c.values(), c.keys()))
        arr.sort()
        ans = ""
        for i in arr:
            ans += i[-1]*i[0]
        return ans[::-1]

# Link: https://leetcode.com/problems/sort-characters-by-frequency/
