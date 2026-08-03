# 1406. Stone Game III
# Hard
# Dynamic Programming
#
# Alice and Bob take turns picking 1, 2, or 3 stones from the front.
# Return "Alice", "Bob", or "Tie" based on optimal play.
#
# Approach: Suffix DP — dp[i] = max score the current player can get from index i onward.
# At each index, the current player tries taking 1, 2, or 3 stones and
# picks the option that maximizes their own score (total remaining - opponent's best).
#
# Time: O(n) | Space: O(n)

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i] = max score the current player can achieve starting from index i
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            take = 0
            for k in range(1, 4):  # take 1, 2, or 3 stones
                if i + k > n:
                    break
                take += stoneValue[i + k - 1]
                # current player gets 'take', opponent gets dp[i+k] from remaining
                # suffix_sum[i] - dp[i] would be opponent's score
                # but we can simplify: dp[i] = max(take - dp[i+k])
                dp[i] = max(dp[i], take - dp[i + k])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
