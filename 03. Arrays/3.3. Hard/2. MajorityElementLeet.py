class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        ca, cb, ea, eb = 0, 0, "x", "x"
        for i in nums:
            if ca == 0 and eb != i:
                ca = 1
                ea = i
            elif cb == 0 and ea != i:
                cb = 1
                eb = i
            elif ea == i:
                ca += 1
            elif eb == i:
                cb += 1
            else:
                ca -= 1
                cb -= 1
        ans = []
        ca, cb = 0, 0
        ca = nums.count(ea)
        cb = nums.count(eb)
        if ca > len(nums) // 3:
            ans.append(ea)
        if cb > len(nums) // 3:
            ans.append(eb)
        return sorted(ans)

# BOYER MOORE's ALGO
# Link: https://leetcode.com/problems/majority-element-ii/
