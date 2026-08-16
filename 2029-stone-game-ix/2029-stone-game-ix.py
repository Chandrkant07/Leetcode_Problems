
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
