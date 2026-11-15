from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1  # empty prefix has even sum
        prefix = 0
        ans = 0
        for x in arr:
            prefix ^= x & 1
            if prefix:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % MOD
