from math import *
from collections import *
from sys import *
from os import *
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Write the code logic here !!!
        ans = []
        restuple = set()

        def helper(arr, idx, n, ds):
            if idx == n:
                ds.sort()
                restuple.add(tuple(ds))
                return
            ds.append(arr[idx])
            helper(arr, idx + 1, n, ds)
            ds.pop()
            helper(arr, idx + 1, n, ds)
        helper(nums, 0, len(nums), [])
        ans = list(map(list, restuple))
        return ans


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()

# Link: https://www.codingninjas.com/studio/problems/get-all-unique-subsets_624393
