"""
2029. Stone Game IX
Medium

Alice and Bob take turns removing stones (Alice first). A player loses if the
sum of removed stones becomes divisible by 3. Bob wins if no stones remain.

Key Insight:
- Only the stone values mod 3 matter. Classify into counts c0, c1, c2.
- Alice can never pick a type-0 stone first (sum would be 0 mod 3 → instant loss).
- Type-0 stones don't change sum mod 3 but flip whose turn it is.

If c0 is even (type-0 stones cancel out):
    Alice wins iff c1 > 0 AND c2 > 0
    (She picks the minority type first, forcing Bob into a losing sequence.)

If c0 is odd (one extra turn flip):
    Alice wins iff abs(c1 - c2) > 2
    (She needs a big enough surplus of one type to survive the turn flip.)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c = [0, 0, 0]
        for s in stones:
            c[s % 3] += 1

        if c[0] % 2 == 0:
            return c[1] > 0 and c[2] > 0
        else:
            return abs(c[1] - c[2]) > 2
