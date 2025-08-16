class Solution:
    def findMatching(self, text, pattern):
        if not pattern:
            return 0
        if len(pattern) > len(text):
            return -1

        l = 0
        while l <= len(text) - len(pattern):
            r = 0
            while r < len(pattern) and text[l + r] == pattern[r]:
                r += 1
            if r == len(pattern):
                return l
            l += 1
        return -1

# Link: https://www.geeksforgeeks.org/problems/index-of-the-first-occurrence-of-pattern-in-a-text/
# Hashing is a technique that is used to uniquely identify a specific object from a group of similar objects. In strings, we use hashing to uniquely identify a substring from a group of substrings. Hashing is a technique that converts a string in a numerical value. This numerical value is used to uniquely identify the string. The hash value of a string is calculated using a hash function. A hash function is a function that converts a string into a numerical value. The hash value of a string is calculated using the hash function. The hash value of a string is unique for each
