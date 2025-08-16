class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c = set(zip(s, t))
        if (len(set(s)) == len(set(t)) == len(c)):
            return True
        return False

# Link: https://leetcode.com/problems/isomorphic-strings/description/
