from typing import List


def quickSort(arr: List[int], start: int, end: int):
    if start >= end:
        return
    p = partition(arr, start, end)
    quickSort(arr, start, p-1)
    quickSort(arr, p+1, end)


def partition(arr, s, e):
    count = 0
    pivot = arr[s]
    for i in range(s+1, e+1):
        if arr[i] <= pivot:
            count += 1

    pivotindex = s + count
    arr[s], arr[pivotindex] = arr[pivotindex], arr[s]

    i, j = s, e

    while i < pivotindex and j > pivotindex:
        while (arr[i] <= pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        if (i < pivotindex and j > pivotindex):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return pivotindex

# Link: https://www.codingninjas.com/studio/problems/quick-sort_5844
