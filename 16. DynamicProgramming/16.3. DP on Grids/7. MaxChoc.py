from typing import List


def function_call(i, ai, bi, r, c, grid, dp):
    if ai < 0 or bi < 0 or ai >= c or bi >= c:
        return -1e8

    if i == r - 1:
        if ai == bi:
            return grid[i][ai]
        return grid[i][ai] + grid[i][bi]

    if dp[i][ai][bi] != -1:
        return dp[i][ai][bi]

    # Explore other paths
    maxi = -1e8
    for dai in range(-1, 2):
        for dbi in range(-1, 2):
            curr_val = 0
            if ai == bi:
                curr_val = grid[i][ai]
            else:
                curr_val = grid[i][ai] + grid[i][bi]
            value = curr_val + function_call(
                i + 1, ai + dai, bi + dbi, r, c, grid, dp)
            maxi = max(maxi, value)

    dp[i][ai][bi] = maxi
    return dp[i][ai][bi]


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp = [[[-1 for _ in range(c)] for _ in range(c)] for _ in range(r)]
    return function_call(0, 0, c-1, r, c, grid, dp)

# Link: https://www.naukri.com/code360/problems/ninja-and-his-friends_3125885
