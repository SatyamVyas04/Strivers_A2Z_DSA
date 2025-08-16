def lps_maker(pattern):
    lps = [0] * len(pattern)
    prevLPS, i = 0, 1
    while i < len(pattern):
        if pattern[i] == pattern[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    return lps


class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = lps_maker(s)
        return s[:lps[-1]]

# Link: https://leetcode.com/problems/longest-happy-prefix/
