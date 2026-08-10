"""
1510. Stone Game IV (Hard)

Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile. On each player's turn, that player
makes a move consisting of removing any non-zero square number of stones.
If a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if Alice wins, assuming both play optimally.

Approach: Dynamic Programming
- dp[i] = True if the current player wins with i stones remaining.
- dp[0] = False (no moves available → current player loses).
- For each i, try removing every perfect square j*j <= i.
  If dp[i - j*j] is False, then current player can force a win → dp[i] = True.

Time Complexity:  O(n * sqrt(n))
Space Complexity: O(n)
"""

from math import isqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]


# --- Testing ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (1, True),
        (2, False),
        (4, True),
        (7, False),
        (17, False),
    ]
    for n, expected in tests:
        result = sol.winnerSquareGame(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} n={n}: got {result}, expected {expected}")
