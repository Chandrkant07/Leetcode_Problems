from collections import Counter
from itertools import permutations

class Solution:
    def totalNumbers(self, digits):
        seen = set()
        n = len(digits)

        for a, b, c in permutations(range(n), 3):
            num = digits[a] * 100 + digits[b] * 10 + digits[c]
            if digits[a] == 0:
                continue
            if digits[c] % 2 != 0:
                continue
            seen.add(num)

        return len(seen)