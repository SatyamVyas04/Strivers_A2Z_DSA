from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    for x in range(0, len(arr)):
        for i in range(0, len(arr)-x-1):
            j = i+1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# Link: https://www.codingninjas.com/studio/problems/bubble-sort_624380