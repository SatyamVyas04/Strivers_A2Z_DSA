from typing import *


def nextGreaterPermutation(arr: List[int]) -> List[int]:
    # Write your code here.
    index = -1
    n = len(arr)
    for ptr in range(n-2, -1, -1):
        if arr[ptr] < arr[ptr + 1]:
            index = ptr
            break
    if index == -1:
        return arr[::-1]

    for i in range(n-1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break
    return arr[:index+1] + arr[index+1:][::-1]

# Link: https://www.codingninjas.com/studio/problems/next-greater-permutation_6929564
