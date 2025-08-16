from typing import List


def selectionSort(arr: List[int]) -> None:
    # Write your code here
    for i in range(len(arr)):
        minimum = arr[i]
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]

# Link: https://www.codingninjas.com/studio/problems/selection-sort_624469
