def twoOddNum(arr):
    xor = 0
    for num in arr:
        xor ^= num

    rightmost_set_bit = xor & ~(xor - 1)

    num1 = 0
    num2 = 0

    for num in arr:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num

    if num1 > num2:
        return [num1, num2]
    else:
        return [num2, num1]

# Link: https://www.codingninjas.com/studio/problems/two-numbers-with-odd-occurrences_8160466?leftPanelTabValue=SUBMISSION
