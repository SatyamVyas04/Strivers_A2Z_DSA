class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        left, right = 0, 1.0

        # Binary search for finding the kth smallest prime fraction
        while left < right:
            # Calculate the middle value
            mid = (left + right) / 2
            # Initialize variables to keep track of maximum fraction and indices
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx, denominator_idx = 0, 0
            j = 1

            # Iterate through the array to find fractions smaller than mid
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1

                # Count smaller fractions
                total_smaller_fractions += (n - j)

                # If we have exhausted the array, break
                if j == n:
                    break

                # Calculate the fraction
                fraction = arr[i] / arr[j]

                # Update max_fraction and indices if necessary
                if fraction > max_fraction:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction

            # Check if we have found the kth smallest prime fraction
            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k:
                right = mid  # Adjust the range for binary search
            else:
                left = mid  # Adjust the range for binary search

        return []  # Return empty list if kth smallest prime fraction not found
