class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 1e9
            if i == j:
                matrix[i][j] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(
                        matrix[i][j], matrix[i][k] + matrix[k][j])
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1e9:
                    matrix[i][j] = -1

# Link: https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
