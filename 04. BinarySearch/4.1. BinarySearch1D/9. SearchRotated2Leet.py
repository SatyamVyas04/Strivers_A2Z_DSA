class Solution:
    def search(self, arr: list[int], k: int) -> bool:
        if len(arr) == 1:
            return arr[0] == k

        low = 0
        high = len(arr) - 1
        ans = 0

        while low <= high:
            mid = (low + high)//2
            if arr[mid] == k or arr[low] == k or arr[high] == k:
                return True
            elif arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
            elif arr[low] <= arr[mid]:
                if arr[low] <= k <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] <= k <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
