def setBits(N: int) -> int:
    temp = N
    count_ones = 0
    while temp:
        if not temp & 1:
            return N + (1 << count_ones)
        else:
            count_ones += 1
            temp >>= 1
    return N

# Link: https://www.codingninjas.com/studio/problems/set-the-rightmost-unset-bit_8160456?leftPanelTabValue=SUBMISSION
