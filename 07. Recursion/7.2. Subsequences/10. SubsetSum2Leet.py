class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def helper(arr, idx, n, ds):
            if idx == n:
                ds.sort()
                res.add(tuple(ds))
                return
            ds.append(arr[idx])
            helper(arr, idx + 1, n, ds)
            ds.pop()
            helper(arr, idx + 1, n, ds)
        helper(nums, 0, len(nums), [])
        return sorted(list(map(list, res)))

# Link: https://leetcode.com/problems/subsets-ii/
