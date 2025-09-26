from typing import *


def rotateMatrix(mat: list[list[int]]):
    # Write your code here.
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(i, m):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        mat[i].reverse()

# Link: https://www.codingninjas.com/studio/problems/rotate-the-matrix_6825090
