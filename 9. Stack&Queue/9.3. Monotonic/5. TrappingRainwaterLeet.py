class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        lmax, rmax = height[0], height[-1]
        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res

# Link: https://leetcode.com/problems/trapping-rain-water/
