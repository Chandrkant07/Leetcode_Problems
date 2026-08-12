"""
2958. Length of Longest Subarray With at Most K Frequency

Sliding window approach:
- Maintain a frequency map for the current window.
- Expand the window by moving the right pointer.
- If any element's frequency exceeds k, shrink from the left.
- Track the maximum valid window size.

Time:  O(n)
Space: O(n)
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        ans = 0

        for right, val in enumerate(nums):
            freq[val] += 1

            while freq[val] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
