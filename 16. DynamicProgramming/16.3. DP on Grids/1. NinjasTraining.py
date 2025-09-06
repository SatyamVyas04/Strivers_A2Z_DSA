# https://www.youtube.com/watch?v=AE39gJYuRog

# Basic Recursion
def recursive_function(day, last, points):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        return maxi

    maxi = 0
    for task in range(3):
        if task != last:
            maxi = max(maxi, points[day][task] +
                       recursive_function(day-1, task, points))
    return maxi


# Memoized
def memo_recursive_function(day, last, points, dp):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        return maxi

    if dp[day][last] != -1:
        return dp[day][last]

    maxi = 0
    for task in range(3):
        if task != last:
            maxi = max(maxi, points[day][task] +
                       memo_recursive_function(day-1, task, points, dp))
    dp[day][last] = maxi

    return dp[day][last]


# Tabulated
def tabulated_approach(n, points, dp):
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            for task in range(3):
                if task != last:
                    point = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], point)

    return dp[n-1][3]


# Space Optimisation
def space_pro_max(n, points):
    prev = [
        max(points[0][1], points[0][2]),
        max(points[0][0], points[0][2]),
        max(points[0][0], points[0][1]),
        max(points[0][0], points[0][1], points[0][2])
    ]

    for day in range(1, n):
        curr = [0 for _ in range(4)]
        for last in range(4):
            for task in range(3):
                if task != last:
                    point = points[day][task] + prev[task]
                    curr[last] = max(curr[last], point)
        prev = curr

    return prev[3]


def ninjaTraining(n: int, points: list[list[int]]) -> int:
    # return recursive_function(n-1, 3, points)

    # dp = [[-1 for _ in range(4)] for _ in range(n)]
    # return memo_recursive_function(n-1, 3, points, dp)

    # dp = [[0 for _ in range(4)] for _ in range(n)]
    # return tabulated_approach(n, points, dp)

    return space_pro_max(n, points)

# Link: https://www.naukri.com/code360/problems/ninja-s-training_3621003
