class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

# Link: https://leetcode.com/problems/merge-sorted-array/
