def rowWithMax1s(matrix: list[list[int]], n: int, m: int) -> int:
    maxCount = 0
    ans = -1

    for i in range(n):
        curr = 0
        if 1 in matrix[i]:
            curr = m - matrix[i].index(1)

        if curr > maxCount:
            ans = i
            maxCount = curr

    return ans

# Link: https://www.codingninjas.com/studio/problems/row-of-a-matrix-with-maximum-ones_982768
