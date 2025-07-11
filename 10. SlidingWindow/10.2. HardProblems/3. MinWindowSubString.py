from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        count = dict(Counter(t))
        window, l, r = {}, 0, 0
        res, resLen = [l, r], float("inf")
        have, need = 0, len(count)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count and window[c] == count[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen != float("inf"):
            return s[l:r+1]
        return ""

# Link: https://leetcode.com/problems/minimum-window-substring/
