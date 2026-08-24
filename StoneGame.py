# 877. Stone Game
# Alice always wins - she can choose all odd or even indexed piles,
# and since total sum is odd, one group is always larger.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]  # dp[i] = net score advantage for current player
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(piles[i] - dp[i+1], piles[i+d] - dp[i])
        return dp[0] > 0
