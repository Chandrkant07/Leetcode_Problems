from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rsum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        # leftBest[i][k] = max over t in [i..k] of (rsum(i,t) + dp[i][t])
        # rightBest[k][j] = max over t in [k..j] of (rsum(t,j) + dp[t][j])
        leftBest = [[0] * n for _ in range(n)]
        rightBest = [[0] * n for _ in range(n)]

        for i in range(n):
            leftBest[i][i] = stoneValue[i]
            rightBest[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Find m: largest k in [i, j-1] with rsum(i,k) <= rsum(k+1,j)
                # Condition: 2*prefix[k+1] <= prefix[j+1] + prefix[i]
                target = prefix[j + 1] + prefix[i]
                lo, hi, m = i, j - 1, i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if 2 * prefix[mid + 1] <= target:
                        m = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                best = 0
                if m < i:
                    # All splits have sum_left > sum_right
                    best = rightBest[i + 1][j]
                elif rsum(i, m) == rsum(m + 1, j):
                    # Equal at m: left side covers [i..m], right side covers [m+1..j]
                    best = max(leftBest[i][m], rightBest[m + 1][j])
                else:
                    # Strict < at m
                    best = leftBest[i][m]
                    if m + 2 <= j:
                        best = max(best, rightBest[m + 2][j])

                dp[i][j] = best

                # Update auxiliary arrays
                leftBest[i][j] = max(leftBest[i][j - 1], rsum(i, j) + dp[i][j])
                rightBest[i][j] = max(rightBest[i + 1][j], rsum(i, j) + dp[i][j])

        return dp[0][n - 1]
