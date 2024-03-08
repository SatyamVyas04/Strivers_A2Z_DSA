def countSetBits(N: int) -> int:
    # Write your code here
    ans = 0
    for i in range(1, N+1):
        ans += bin(i)[2:].count("1")
    return ans

# def countSetBits(N):
#     # We have 'd' which is the size of repeating window.
#     # We are using 'x' to run the loop Log(N) times which is equal to the number of bits in its binary representation.
#     d = 2
#     ans = 0
#     x = N
#     while x:
#         # Using the Mathematical formula explained in the Approach.
#         ans += ((N + 1) // d) * (d // 2) + max((N + 1) % d - d // 2, 0)

#         # Window size double every time we shift to the next left bit.
#         d *= 2
#         x //= 2
#     return ans

# Link: https://www.codingninjas.com/studio/problems/count-total-set-bits_784?leftPanelTabValue=SOLUTION