class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []  # (Greater Element is placed here)
        n = len(nums)
        ans = [-1] * n
        nums = nums + nums

        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack:
                ans[i % n] = -1
            else:
                ans[i % n] = stack[-1]
            stack.append(nums[i])
        return ans


# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         nge = [-1] * n
#         st = []


#         for i in range(2 * n - 1, -1, -1):
#             while st and st[-1] <= nums[i % n]:
#                 st.pop()


#             if i < n:
#                 if st:
#                     nge[i] = st[-1]
#             st.append(nums[i % n])
#         return nge


# Link: https://leetcode.com/problems/next-greater-element-ii/description/
