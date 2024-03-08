def isPowerOfTwo(n: int) -> bool:
    # Write your code here
    count = 0
    while n:
        count += n & 1
        n >>= 1
        if count > 1:
            return False
    return True

# Link: https://www.codingninjas.com/studio/problems/power-of-two_893061?leftPanelTabValue=SUBMISSION
