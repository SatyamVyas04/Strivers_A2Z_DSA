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


def kmp(pattern, text, lps):
    l, r = 0, 0
    while l < len(text):
        if text[l] == pattern[r]:
            l, r = l + 1, r + 1
        else:
            if r == 0:
                l += 1
            else:
                r = lps[r - 1]
        if r == len(pattern):
            return l - len(pattern)
    return -1

class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        lps = lps_maker(needle)
        return kmp(needle, haystack, lps)
    
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/