class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return (len(s) == len(goal) and goal in s + s)

# Link: https://leetcode.com/problems/rotate-string/
