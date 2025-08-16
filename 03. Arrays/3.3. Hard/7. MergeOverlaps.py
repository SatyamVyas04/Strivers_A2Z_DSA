from typing import *


def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
    # Write your code here.
    arr.sort()
    ans = []
    for i in arr:
        if ans == []:
            ans.append(i)
            continue

        if i[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], i[1])
        else:
            ans.append(i)

    return ans

# Link: https://www.codingninjas.com/studio/problems/merge-all-overlapping-intervals_6783452
