import functools

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate the bitwise XOR of all elements
        # Using functools.reduce for conciseness, handle empty list edge case explicitly if needed
        # Constraints state 1 <= nums.length, so nums will not be empty.
        total_xor = 0
        if n > 0: # This check is redundant due to constraints but good practice
            total_xor = functools.reduce(lambda a, b: a ^ b, nums)

        # Case 1: The XOR sum of the entire array is non-zero.
        # The longest subsequence is the entire array.
        if total_xor != 0:
            return n
        
        # Case 2: The XOR sum of the entire array is zero.
        # We cannot use the entire array. We try to form a subsequence of length n-1.
        # If we remove one element 'x', the XOR sum of the remaining elements will be 0 ^ x = x.
        # So, if there's any non-zero element 'x' in nums, we can remove it,
        # and the remaining n-1 elements will have a non-zero XOR sum.
        # This will be the longest possible length (n-1) in this case.
        
        # Check if there is at least one non-zero element in nums.
        for num in nums:
            if num != 0:
                # Found a non-zero element. We can remove it to get a non-zero XOR sum.
                return n - 1
        
        # If we reach here, it means total_xor was 0, AND all elements in nums are 0.
        # In this situation, no subsequence can have a non-zero XOR sum.
        return 0