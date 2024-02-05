def bitManipulation(num: int, i: int) -> list[int]:
    # Write your code here.
    ans1 = num >> (i-1) & 1
    ans2 = num | 1 << i-1
    ans3 = num & ~(1 << i-1)
    return [ans1, ans2, ans3]

# Link: https://www.codingninjas.com/studio/problems/bit-manipulation_8142533