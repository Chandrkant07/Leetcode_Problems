from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_num = min(nums1)

        # If all numbers have the same parity
        all_same_parity = all(x % 2 == nums1[0] % 2 for x in nums1)

        # Possible if all same parity OR minimum number is odd
        return all_same_parity or min_num % 2 == 1