class Solution:
    def minimumPlatform(self, n, arr, dep):
        ans = 0
        plat = 0
        arr.sort()
        dep.sort()
        l, r = 0, 0  # l for arr, r for dep
        while l < n and r < n:
            if arr[l] <= dep[r]:
                plat += 1
                ans = max(plat, ans)
                l += 1
            else:
                plat -= 1
                r += 1
        return ans


sol = Solution()
print(sol.minimumPlatform(6, [900, 940, 950, 1100, 1500, 1800], [
      910, 1200, 1120, 1130, 1900, 2000]))

# Link: https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
