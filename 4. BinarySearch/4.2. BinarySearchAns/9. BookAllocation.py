def pagescheck(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr: [int], n: int, m: int) -> int:
    # Write your code here
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        count = pagescheck(arr, mid)
        if count > m:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Link: https://www.codingninjas.com/studio/problems/allocate-books_1090540