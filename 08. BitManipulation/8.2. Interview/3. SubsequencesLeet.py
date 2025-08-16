class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        length = 1 << len(nums)
        for i in range(0, length):
            current_num = bin(i)[2:].zfill(len(nums))
            current_str = self.return_int_to_str(nums, current_num)
            ans.append(current_str)
        return sorted(ans)

    def return_int_to_str(self, string, num):
        ans = []
        for i in range(len(string)):
            if num[i] == "1":
                ans.append(string[i])
        return ans

# Link: https://leetcode.com/problems/subsets/
