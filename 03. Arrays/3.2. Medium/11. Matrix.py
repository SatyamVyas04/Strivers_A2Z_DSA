from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    # Write your code here.
    rowb = []
    colb = []
    for i in range(n):
        for j in range(m):
            element = matrix[i][j]
            if element == 0:
                if i not in rowb:
                    rowb.append(i)
                if j not in colb:
                    colb.append(j)
    for i in range(n):
        for j in range(m):
            if i in rowb or j in colb:
                matrix[i][j] = 0
                
    return matrix

# Link: https://www.codingninjas.com/studio/problems/zero-matrix_1171153