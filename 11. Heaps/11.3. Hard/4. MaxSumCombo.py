import heapq


class Solution:
    def solve(self, a, b, k):
        n = len(a)
        # Sorting the arrays.
        a.sort()
        b.sort()

        # Using a max-heap.
        maxHeap = []
        heapq.heappush(maxHeap, (-(a[n - 1] + b[n - 1]), n - 1, n - 1))

        # Using a set.
        mySet = set([(n - 1, n - 1)])

        # Output array to store the K max sum combinations.
        result = []

        while k > 0:
            sum_val, x, y = heapq.heappop(maxHeap)
            sum_val = -sum_val  # Negate the value back to positive

            # Add the sum to the output array.
            result.append(sum_val)

            # Check if the indices (x-1, y) are present in the set.
            if (x - 1, y) not in mySet:
                heapq.heappush(maxHeap, (-(a[x - 1] + b[y]), x - 1, y))
                mySet.add((x - 1, y))

            # Check if the indices (x, y-1) are present in the set.
            if (x, y - 1) not in mySet:
                heapq.heappush(maxHeap, (-(a[x] + b[y - 1]), x, y - 1))
                mySet.add((x, y - 1))

            k -= 1

        # Return the output array.
        return result

# Link: https://www.interviewbit.com/problems/maximum-sum-combinations/
