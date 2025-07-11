class Solution:
    def solveSudoku(self, board: list[list[str]]) -> bool:
        def isvalid(row, col, k):
            for i in range(9):
                if board[row][i] == k:
                    return False
                if board[i][col] == k:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i % 3] == k:
                    return False
            return True

        def solve(board) -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if isvalid(i, j, f"{num}"):
                                board[i][j] = f"{num}"
                                if solve(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True
        return solve(board)

# Link: https://leetcode.com/problems/sudoku-solver/
