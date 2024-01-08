class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    
# Link: https://leetcode.com/problems/reverse-words-in-a-string/