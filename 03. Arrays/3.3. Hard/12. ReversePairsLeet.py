class Solution:
    def reversePairs(self, nums: [int]) -> int:

        def ms(l, r):
            if l >= r:
                return 0
            mid = (l + r) // 2
            count = ms(l, mid) + ms(mid + 1, r)

            j = mid + 1
            for i in range(l, mid+1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid - 1

            nums[l:r+1] = sorted(nums[l:r+1])
            return count

        return ms(0, len(nums) - 1)

# Link: https://leetcode.com/problems/reverse-pairs/
