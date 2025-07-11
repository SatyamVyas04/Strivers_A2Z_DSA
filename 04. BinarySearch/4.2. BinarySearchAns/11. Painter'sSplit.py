def checkfn(arr, cap):
    c = 1
    total = 0
    for i in arr:
        if total + i <= cap:
            total += i
        else:
            total = i
            c += 1
    return c

def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    if k > len(boards):
        return -1
    low = max(boards)
    high = sum(boards)
    while low <= high:
        mid = (low + high)//2
        check = checkfn(boards, mid)
        if check > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Link: https://www.codingninjas.com/studio/problems/painter-s-partition-problem_1089557