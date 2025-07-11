from typing import List


def ratMaze(matrix: List[List[int]]) -> List[str]:
    n = len(matrix)
    res = []

    def is_valid_move(r, c):
        return 0 <= r < n and 0 <= c < n and matrix[r][c] == 1

    def helper(r, c, ds):
        if r == n - 1 and c == n - 1:
            res.append("".join(ds))
            return

        directions = [(0, 1, "R"), (0, -1, "L"), (1, 0, "D"), (-1, 0, "U")]

        for dr, dc, move in directions:
            new_r, new_c = r + dr, c + dc
            if is_valid_move(new_r, new_c) and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                ds.append(move)
                helper(new_r, new_c, ds)
                ds.pop()
                visited.remove((new_r, new_c))

    visited = {(0, 0)}
    helper(0, 0, [])
    return res

# Link: https://www.codingninjas.com/studio/problems/rat-in-a-maze-_8842357