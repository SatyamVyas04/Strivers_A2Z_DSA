def missingNumber(n: int, arr: list[int]) -> int:
    # Write your code here
    ans = 0
    for i in arr:
        ans ^= i
    return ans

# Link: https://www.codingninjas.com/studio/problems/one-odd-occurring_4606074?leftPanelTabValue=SUBMISSION
