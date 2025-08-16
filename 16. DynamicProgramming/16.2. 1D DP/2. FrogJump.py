def frogJump(n: int, heights: list[int]) -> int:
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])

    for i in range(2, n):
        one_jump = dp[i-1] + abs(heights[i] - heights[i-1])
        two_jump = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(one_jump, two_jump)

    return dp[n-1]

# Link: https://www.naukri.com/code360/problems/frog-jump_3621012?leftPanelTabValue=SUBMISSION
