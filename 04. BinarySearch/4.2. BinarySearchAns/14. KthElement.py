def kthElement(a: list[int], n1: int, b: list[int], n2: int, k: int) -> int:
    # Write your code from here.
    if n1 > n2:
        a, b = b, a
        n1, n2 = n2, n1

    low, high = max(k-n2, 0), min(n1, k)
    n = n1 + n2
    left = k
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
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return -1

# Link: https://www.codingninjas.com/studio/problems/k-th-element-of-2-sorted-array_1164159
