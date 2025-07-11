def cowscheck(stalls, dist, cows):
    cntcows = 1
    n = len(stalls)
    lastplaced = stalls[0]
    for i in range(1, n):
        if stalls[i] - lastplaced >= dist:
            lastplaced = stalls[i]
            cntcows += 1
        if cntcows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    low = 0
    high = stalls[-1] - stalls[0]
    while low <= high:
        mid = (low + high) // 2
        if cowscheck(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

# Link: https://www.codingninjas.com/studio/problems/aggressive-cows_1082559