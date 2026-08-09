"""
1140. Stone Game II
Medium

Alice and Bob continue their games with piles of stones.
On each player's turn, that player can take all the stones in the first X remaining piles,
where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.
Assuming both play optimally, return the maximum number of stones Alice can get.

Approach: Suffix sum + memoized DP
- dp(i, m) = max stones the current player can collect from piles[i:] with parameter M = m
- The current player tries all X in [1, 2*m], takes suffix[i] - suffix[i+X],
  and the opponent then gets dp(i+X, max(m, X)) from the remainder.
- Current player's gain = suffix[i] - dp(i+X, max(m, X))

Time:  O(n^3)  — at most O(n^2) states, each iterating up to O(n) choices
Space: O(n^2)
"""

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
