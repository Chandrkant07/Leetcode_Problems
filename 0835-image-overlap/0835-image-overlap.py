from typing import List
from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ones1 = [(r, c) for r in range(len(img1)) for c in range(len(img1)) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(len(img2)) for c in range(len(img2)) if img2[r][c] == 1]

        shifts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shifts[(r2 - r1, c2 - c1)] += 1

        return max(shifts.values(), default=0)