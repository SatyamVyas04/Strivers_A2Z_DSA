def mergeSort(arr: [int], l: int, r: int):
    if l < r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    len1 = mid - l + 1
    len2 = r - mid

    first = arr[l:mid + 1]
    second = arr[mid + 1:r + 1]

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if first[i] < second[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = first[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = second[j]
        j += 1
        k += 1

    return arr

# Link: https://www.codingninjas.com/studio/problems/merge-sort_5846
