class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        n = len(nums)

        if n == 0:
            return (-1, -1)
        if n == 1:
            if nums[0] == target:
                return (0, 0)
            else:
                return (-1, -1)

        low = 0
        high = n-1
        a, b = -1, n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                a = mid
                high = mid - 1
            else:
                low = mid + 1

        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                b = mid
                high = mid - 1
            else:
                low = mid + 1

        if nums[a] != target:
            return (-1, -1)
        return (a, b-1)

# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
