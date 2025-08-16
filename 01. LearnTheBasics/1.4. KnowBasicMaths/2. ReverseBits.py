def reverseBits(n):
    # Write your code here.
    return int(bin(n)[2:].zfill(32)[::-1], 2)

# Link: https://www.codingninjas.com/studio/problems/reverse-bits_2181102
