class Solution:
    def generate(self, numRows: int) -> [[int]]:
        soln = []
        for i in range(1, numRows+1):
            soln.append(self.generaterow(i))
        return soln
    
    def generaterow(self, n):
        ans = [1]
        term = 1
        for i in range(1, n):
            term = term * (n-i)
            term //= i
            ans.append(term)
        return ans

# Link: https://leetcode.com/problems/pascals-triangle/