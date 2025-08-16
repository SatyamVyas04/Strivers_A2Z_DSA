class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        letters = [0] * 3  # a, b, c
        ans = 0
        l = 0
        for r in range(len(s)):
            r_idx = ord(s[r]) - 97
            letters[r_idx] += 1
            while all(letters):
                ans += len(s) - r
                l_idx = ord(s[l]) - 97
                letters[l_idx] -= 1
                l += 1
        return ans

# Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
