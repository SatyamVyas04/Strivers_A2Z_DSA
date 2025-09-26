def fourSum(nums: list[int], target: int) -> list[list[int]]:
    # Write your code from here.
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j != i+1 and nums[j] == nums[j-1]:
                continue
            k = j+1
            l = n-1
            while k < l:
                s = nums[i]
                s += nums[j]
                s += nums[k]
                s += nums[l]
                if s == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    l -= 1
                    k += 1
                    while (k < l and nums[k] == nums[k-1]):
                        k += 1
                    while (k < l and nums[l] == nums[l+1]):
                        l -= 1
                elif s > target:
                    l -= 1
                else:
                    k += 1
    return ans

# Link: https://www.codingninjas.com/studio/problems/4sum_5713771
