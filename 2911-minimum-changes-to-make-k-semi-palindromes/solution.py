class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")

        def changes(sub: str) -> int:
            m = len(sub)
            best = INF
            for d in range(1, m):
                if m % d:
                    continue
                cost = 0
                for r in range(d):
                    g = sub[r::d]
                    for a in range(len(g) // 2):
                        if g[a] != g[len(g) - 1 - a]:
                            cost += 1
                best = min(best, cost)
            return best

        # cost[i][j]: changes to make s[i..j] a semi-palindrome (length >= 2)
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = changes(s[i:j + 1])

        # dp[p][j]: min changes for first j chars split into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] < INF:
                        c = dp[p - 1][i] + cost[i][j - 1]
                        if c < dp[p][j]:
                            dp[p][j] = c
        return dp[k][n]
