class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        # Compute prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # dp tracks the best score difference achievable
        # when the current player's minimum choosable index is i.
        # Base case: dp[n-1] = prefix[n-1] (only one choice left)
        dp = stones[n - 1]

        # Iterate from right to left: either pick prefix[i] (gain prefix[i] - dp)
        # or skip to dp (same value carried forward)
        for i in range(n - 2, 0, -1):
            dp = max(stones[i] - dp, dp)

        return dp
