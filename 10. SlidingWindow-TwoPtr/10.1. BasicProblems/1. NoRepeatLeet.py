from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        dic = defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            dic[s[r]] += 1
            while dic[s[r]] == 2:
                dic[s[l]] -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
            r += 1
        return ans
    
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/