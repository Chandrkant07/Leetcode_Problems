class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # If all numbers already have the same parity
        even_count = sum(x % 2 == 0 for x in nums1)
        odd_count = len(nums1) - even_count
        
        # All even or all odd
        if even_count == 0 or odd_count == 0:
            return True
        
        # If both even and odd numbers exist, we can make
        # every element odd using subtraction where needed.
        return len(nums1) > 1