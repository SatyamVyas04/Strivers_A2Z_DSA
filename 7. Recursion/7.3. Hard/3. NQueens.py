from typing import List


def nQueens(n: int) -> List[List[int]]:
    chess = [[0 for _ in range(n)] for _ in range(n)]
    res = []

    def place(row, col, chess, n):
        duprow = row
        dupcol = col
        while row >= 0 and col >= 0:
            if chess[row][col] == 1:
                return False
            row -= 1
            col -= 1
        row = duprow
        col = dupcol
        while col >= 0:
            if chess[row][col] == 1:
                return False
            col -= 1
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if chess[row][col] == 1:
                return False
            row += 1
            col -= 1
        return True

    def checking(col, chess, res, n):
        if col == n:
            newchess = []
            for i in chess:
                newchess += i
            res.append(newchess)
            return
        for row in range(n):
            if place(row, col, chess, n):
                chess[row][col] = 1
                checking(col+1, chess, res, n)
                chess[row][col] = 0
    checking(0, chess, res, n)
    return res

# Link:https://www.codingninjas.com/studio/problems/n-queens_696453
