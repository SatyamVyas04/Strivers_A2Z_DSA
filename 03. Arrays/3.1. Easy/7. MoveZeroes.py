def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    i = 0
    while i < n:
        if a[i] == 0:
            a.pop(i)
            a.append(0)
            i -= 1
            n -= 1
        i += 1
    return a

# Link: https://www.codingninjas.com/studio/problems/ninja-and-the-zero-s_6581958
