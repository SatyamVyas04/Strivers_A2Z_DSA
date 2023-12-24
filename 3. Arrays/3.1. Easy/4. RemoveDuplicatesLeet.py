class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        s = sorted(list(set(nums)))
        nums[:len(nums)-len(s)] = s
        return len(s)
    
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/