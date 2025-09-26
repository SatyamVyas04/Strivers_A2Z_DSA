# Contributing to Striver's A2Z DSA Sheet Solutions

Thank you for considering contributing to this repository! This document outlines the guidelines for contributing solutions to Striver's A2Z DSA Sheet.

## Code of Conduct

Please be respectful and considerate when contributing. Help us maintain a positive and inclusive environment for everyone.

## How to Contribute

### Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/SatyamVyas04/Strivers_A2Z_DSA.git`
3. Create a new branch: `git checkout -b solution/problem-name`

### Adding a Solution

1. Check if the problem already has a solution in Python
2. If not, you can add it following our directory structure
3. If it exists, you can optimize the existing solution or provide an alternative approach

### Solution Structure

Each solution should:

1. Include the problem statement as a comment
2. Have proper time and space complexity analysis
3. Include explanatory comments for complex logic
4. Follow language-specific best practices

Example:

```python
"""
Problem: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    # Create a hash map to store values and their indices
    hash_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed
        complement = target - num

        # If complement exists in hash map, return both indices
        if complement in hash_map:
            return [hash_map[complement], i]

        # Store current number and its index
        hash_map[num] = i

    # If no solution found
    return []
```

## Pull Request Process

1. Ensure your code follows the standards mentioned above
2. Update the README.md with details of your solution if necessary
3. Submit a pull request with a clear description of your solution
4. Wait for review and address any feedback

## Language Support

We welcome solutions in Python, just to maintain consistency with the existing codebase. We wish to expand in the following languages:

- C++
- Java
- JavaScript
- Other languages (please maintain consistency with existing solutions)

## Additional Guidelines

- Do not submit solutions without proper explanation
- Include multiple approaches if possible (Brute Force, Optimized, etc.)
- For each approach, mention time and space complexity

Thank you for your contributions!
