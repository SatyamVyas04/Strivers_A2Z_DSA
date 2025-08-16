from typing import List


def present(board: List[List[str]], word: str, rows: int, cols: int) -> bool:
    # Write your code here
    rows, cols = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0) or (c < 0) or (r >= rows) \
            or (c >= cols) or (word[i] != board[r][c]) \
                or ((r, c) in path):
            return False

        path.add((r, c))
        res = dfs(r+1, c, i+1) or dfs(r, c+1, i+1) \
            or dfs(r-1, c, i+1) or dfs(r, c-1, i+1)
        path.remove((r, c))
        return res

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

# Link: https://www.codingninjas.com/studio/problems/word-search---l_892986
