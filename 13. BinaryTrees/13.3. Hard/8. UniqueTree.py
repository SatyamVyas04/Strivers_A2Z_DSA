class Solution:
    def isPossible(self, a, b):
        if a > b:
            a, b = b, a
        
        if (a == 1 and b == 2) or (a == 2 and b == 3):
            return 1
        else:
            return 0
    
# Link: https://www.geeksforgeeks.org/problems/unique-binary-tree-requirements/1