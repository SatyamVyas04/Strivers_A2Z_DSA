from fractions import Fraction


class Solution:
    def searchInsert(self, nums: list[Fraction], target) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if float(nums[mid]) == float(target):
                return mid
            if float(nums[mid]) < float(target):
                l = mid+1
            else:
                r = mid-1
        return l

    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        ans = [Fraction(0, 1)]
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                f = Fraction(arr[i], arr[j])
                idx = self.searchInsert(ans, f)
                ans.insert(idx, f)
        return [ans[k].numerator, ans[k].denominator]


# Tried
