def search(nums: list[int], target: int):
    # write your code logic !!
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
target = int(input())
print(search(arr, target))

# Link: https://www.codingninjas.com/studio/problems/binary-search_972
