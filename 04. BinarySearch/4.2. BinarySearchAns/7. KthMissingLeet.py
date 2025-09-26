class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k

# Link: https://leetcode.com/problems/kth-missing-positive-number/
