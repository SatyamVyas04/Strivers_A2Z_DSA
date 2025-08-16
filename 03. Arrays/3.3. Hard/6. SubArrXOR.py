"""
    Time Complexity: O( N )
    Space Complexity: O( N )

    where N is the size of array 'A'
"""


def subarraysWithSumK(a: [int], b: int) -> int:
    count = 0
    # number of subarrays
    # whose XOR is equal to ‘b’

    countXOR = {}  # storing the frequency of
    # some bitwise XOR.
    curr = 0
    n = len(a)  # Size of array 'a'
    for i in range(n):
        curr ^= a[i]
        if curr == b:
            count += 1

        temp = curr ^ b
        val = 0
        if temp in countXOR:
            val = countXOR[temp]
        count += val
        if not curr in countXOR:
            countXOR[curr] = 0
        countXOR[curr] += 1
    return count

# Link: https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258
