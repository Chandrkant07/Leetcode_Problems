from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i: int, m: int) -> int:
            """Max stones the current player can collect from piles[i:] with M = m."""
            if i >= n:
                return 0
            # If the current player can take everything remaining
            if i + 2 * m >= n:
                return suffix[i]
            best = 0
            for x in range(1, 2 * m + 1):
                # Current player takes piles[i:i+x], opponent gets dp(i+x, max(m,x))
                best = max(best, suffix[i] - dp(i + x, max(m, x)))
            return best

        return dp(0, 1)
