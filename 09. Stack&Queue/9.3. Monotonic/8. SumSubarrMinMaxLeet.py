from operator import gt, lt


class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:

        def fn(op):
            """Return min sum (if given gt) or max sum (if given lt)."""
            ans = 0
            stack = []
            for i in range(len(nums) + 1):
                while stack and (i == len(nums) or op(nums[stack[-1]], nums[i])):
                    mid = stack.pop()
                    ii = stack[-1] if stack else -1
                    ans += nums[mid] * (i - mid) * (mid - ii)
                stack.append(i)
            return ans

        return fn(lt) - fn(gt)

# Link: https://leetcode.com/problems/sum-of-subarray-ranges/
