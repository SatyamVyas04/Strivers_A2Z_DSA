from bisect import bisect_right
def median(matrix: list[list[int]], m: int, n: int) -> int:
    maximum = int("-inf")
    minimum = int("inf")

    # To find the minimum and maximum in the matrix
    for i in range(m):
        if matrix[i][0] < minimum:
            minimum = matrix[i][0]
        if matrix[i][n - 1] > maximum:
            maximum = matrix[i][n - 1]

    # Count for the number to be the median
    checkCount = (m * n + 1) // 2

    # Binary search for the median
    while minimum < maximum:
        mid = minimum + (maximum - minimum) // 2
        count = 0
        find = 0
        for i in range(m):
            # Binary search for finding the count in each row
            find = bisect_right(matrix[i], mid)
            # Increment count
            count = count + find
        if count < checkCount:
            minimum = mid + 1
        else:
            maximum = mid

    # Finally return the answer
    return minimum

# Link: https://www.codingninjas.com/studio/problems/median-of-a-row-wise-sorted-matrix_1115473