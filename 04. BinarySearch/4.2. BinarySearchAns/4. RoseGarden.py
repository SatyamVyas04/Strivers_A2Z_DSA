def possible(arr, day, m, k):
    n = len(arr)
    cnt = 0
    noOfB = 0
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m


def roseGarden(arr, k, m):
    val = m * k
    n = len(arr)
    if val > n:
        return -1

    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    low = mini
    high = maxi
    while low <= high:
        mid = (low + high) // 2
        if possible(arr, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low

# Link: https://www.codingninjas.com/studio/problems/rose-garden_2248080
