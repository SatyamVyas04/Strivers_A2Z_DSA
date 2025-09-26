class Solution:
    def findPeakGrid(self, arr: list[list[int]]) -> list[int]:
        n = len(arr)  # Size of the array
        m = len(arr[0])

        # Extra Optimised Case
        if n == 1 and m == 1:
            return [0, 0]

        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high)//2

            index = -1
            maxval = -1
            for i in range(n):
                if arr[i][mid] > maxval:
                    maxval = arr[i][mid]
                    index = i

            l = arr[index][mid - 1] if mid-1 >= 0 else -1
            r = arr[index][mid + 1] if mid+1 < m else -1

            if arr[index][mid] > l and arr[index][mid] > r:
                return [index, mid]
            elif arr[index][mid] < l:
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]

# Link: https://leetcode.com/problems/find-a-peak-element-ii/
