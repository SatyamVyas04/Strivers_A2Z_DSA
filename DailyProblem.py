class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        max_found = False
        min_found = False
        prev_max_index = 0
        prev_min_index = 0
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            if not (minK <= num <= maxK):
                max_found = False
                min_found = False
                left = right + 1
            if num == minK:
                min_found = True
                prev_min_index = right
            if num == maxK:
                max_found = True
                prev_max_index = right
            if max_found and min_found:
                ans += min(prev_max_index, prev_min_index) - left + 1
        return ans


sol = Solution()
print(sol.countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))
