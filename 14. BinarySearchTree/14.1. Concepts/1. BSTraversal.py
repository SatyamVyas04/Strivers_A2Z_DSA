class Solution:
    def isBSTTraversal(self, arr):
        mini = float("-inf")
        for num in arr:
            if num <= mini:
                return False
            mini = num
        return True

# Link: https://www.geeksforgeeks.org/problems/binary-search-trees/1
