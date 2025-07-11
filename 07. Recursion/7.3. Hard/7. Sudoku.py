def sudokuSolver(board: list[list[int]]) -> bool:
    # Write your code here
    def safe(row, col, k, board):
        for i in range(9):
            if board[row][i] == k:
                return False
            if board[i][col] == k:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i % 3] == k:
                return False
        return True

    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for k in range(1, 10):
                        if safe(i, j, k, board):
                            board[i][j] = k
                            if solve(board):
                                return True
                            board[i][j] = 0
                    return False
        return True
    return solve(board)

# Link: https://www.codingninjas.com/studio/problems/sudoku-solver_8416969
