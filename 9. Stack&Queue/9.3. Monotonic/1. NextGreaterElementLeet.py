class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        index_map = {num: idx for idx, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                result[index_map[smaller_num]] = num
            if num in index_map:
                stack.append(num)

        return result

# Link: https://leetcode.com/problems/next-greater-element-i/
