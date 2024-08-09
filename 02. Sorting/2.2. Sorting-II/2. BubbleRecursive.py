from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    if n==1: return
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubbleSort(arr, n-1)
    
# Link: https://www.codingninjas.com/studio/problems/bubble-sort_624380