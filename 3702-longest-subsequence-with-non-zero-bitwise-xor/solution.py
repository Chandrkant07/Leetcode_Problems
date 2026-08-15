import functools
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate the bitwise XOR of all elements
        total_xor = functools.reduce(lambda a, b: a ^ b, nums)

        # Case 1: XOR of entire array is non-zero → use all elements
        if total_xor != 0:
            return n

        # Case 2: XOR of entire array is zero
        # Removing one non-zero element flips the XOR to non-zero (n-1 elements)
        # If all elements are zero, no subsequence can have non-zero XOR
        if any(x != 0 for x in nums):
            return n - 1

        return 0
