class Solution:
    def rotate(self, arr: [int], k: int) -> None:
        k = k%len(arr)
        arr[:] = arr[-k:] + arr[:-k]
        
# Link: https://leetcode.com/problems/rotate-array/description/