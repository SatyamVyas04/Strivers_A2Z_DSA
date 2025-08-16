class Solution:
    def findMedianSortedArrays(self, a: [int], b: [int]) -> float:
        n1 = len(a)
        n2 = len(b)
        if n1 > n2:
            a, b = b, a
            n1, n2 = n2, n1

        low, high = 0, n1
        left = (n1 + n2 + 1) // 2
        n = n1 + n2
        while low <= high:
            mid1 = (low + high)//2
            mid2 = left - mid1
            l1 = float("-inf")
            l2 = float("-inf")
            r1 = float("inf")
            r2 = float("inf")
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1-1 >= 0:
                l1 = a[mid1-1]
            if mid2-1 >= 0:
                l2 = b[mid2-1]
            if (l1 <= r2) and (l2 <= r1):
                if n % 2 == 1:
                    return float(max(l1, l2))
                else:
                    return float((max(l1, l2) + min(r1, r2))/2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return -1

# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
