class Solution:
    def findMin(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]

        low = 0
        high = n-1
        ans = float("inf")

        while low <= high:
            mid = (low + high) // 2
            if arr[low] <= arr[mid]:
                ans = min(arr[low], ans)
                low = mid + 1
            else:
                ans = min(arr[mid], ans)
                high = mid - 1
        return ans

# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
