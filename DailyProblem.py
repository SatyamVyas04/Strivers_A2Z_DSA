# from sortedcontainers import SortedList


# class Solution:
#     def longestSubarray(self, nums: list[int], limit: int) -> int:
#         ans = 0
#         n = len(nums)
#         sl = SortedList()

#         l = 0
#         for r in range(n):
#             sl.add(nums[r])
#             while sl[-1] - sl[0] > limit:  # type: ignore
#                 sl.remove(nums[l])
#                 l += 1
#             ans = max(ans, r - l + 1)

#         return ans


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain the max_deque in decreasing order
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Maintain the min_deque in increasing order
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            # Check if the current window exceeds the limit
            while max_deque[0] - min_deque[0] > limit:
                # Remove the elements that are out of the current window
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


sol = Solution()
print(sol.longestSubarray(nums=[8, 2, 4, 7], limit=4))
print(sol.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
print(sol.longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))
print(sol.longestSubarray(nums=[1, 5, 6, 7, 8, 10, 6, 5, 6], limit=4))
