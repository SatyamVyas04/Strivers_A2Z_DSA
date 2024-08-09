def findXOR(L: int, R: int) -> int:
    # Write your code here.
    xor = 0
    for i in range(L, R+1):
        xor ^= i
    return xor

# Link: https://www.codingninjas.com/studio/problems/l-to-r-xor_8160412?leftPanelTabValue=SUBMISSION