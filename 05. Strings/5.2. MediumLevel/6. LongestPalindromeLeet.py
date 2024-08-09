class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        def check(s, l, r, i):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > self.maxl:
                    self.maxi = s[l:r+1]
                    self.maxl = max(self.maxl, r-l+1) 
                l -= 1
                r += 1
        
        self.maxi = ""
        self.maxl = 0
        for i in range(len(s)):
            l, r = i, i
            check(s, l, r, i)
            l, r = i, i+1
            check(s, l, r, i)
        return self.maxi
            
# Link: https://leetcode.com/problems/longest-palindromic-substring/