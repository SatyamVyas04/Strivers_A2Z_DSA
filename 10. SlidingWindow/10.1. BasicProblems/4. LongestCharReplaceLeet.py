from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        l, r = 0, 0
        max_freq = 0
        ans = 0
        while r < len(s):
            dic[s[r]] += 1
            max_freq = max(max_freq, dic[s[r]])
            if (r - l + 1) - max_freq <= k:
                ans = max(ans, r - l + 1)
            else:
                dic[s[l]] -= 1
                l += 1
            r += 1
        return ans

# Link: https://leetcode.com/problems/longest-repeating-character-replacement/