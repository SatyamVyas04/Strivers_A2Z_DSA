'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    where N is the size of array 'A'.
'''


def subarraysWithSumK(a: [int], k: int) -> [[int]]:
    n = len(a)
    ans = []
    # This will keep all those sub-arrays whose sum = ‘k’.
    # start and end are the starting
    # and the ending indices of our current
    # subarray
    start = 0
    end = -1
    currentSum = 0

    # Iterating over 'a'
    while (start < n):
        # Increasing the right end
        # till our sum <= ‘k’ or
        # we are not out of bounds
        while ((end + 1 < n) and (currentSum + a[end + 1] <= k)):
            currentSum += a[end + 1]
            end += 1
        # We have found a subarray with the
        # required sum.
        if (currentSum == k):
            temp = []
            for i in range(start, end+1):
                temp.append(a[i])
            ans.append(temp[:])

        # Shifting the start index
        currentSum -= a[start]
        start += 1

    return ans

# Link: https://www.codingninjas.com/studio/problems/subarrays-with-sum-‘k'_6922076
