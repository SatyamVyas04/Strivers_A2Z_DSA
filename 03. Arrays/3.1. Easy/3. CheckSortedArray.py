def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return 0
    return 1

# Link: https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957
