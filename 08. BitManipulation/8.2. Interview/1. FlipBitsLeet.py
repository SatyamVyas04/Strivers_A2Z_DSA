class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')

# Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number
