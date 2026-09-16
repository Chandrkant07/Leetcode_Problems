import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # Direct math.comb computes the combinations efficiently
        return math.comb(n + k - 1, 2 * k) % MOD
