def flipBits(A: int, B: int) -> int:
    # Write your code here.
    xorres = A ^ B
    count = 0
    while xorres:
        count += xorres & 1
        xorres >>= 1
    return count

# Link: https://www.codingninjas.com/studio/problems/flip-bits_8160405?leftPanelTabValue=SUBMISSION
