class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")

        def semi_cost(sub: str) -> int:
            m = len(sub)
            best = INF
            for d in range(1, m):
                if m % d:
                    continue
                changes = 0
                for r in range(d):
                    grp = sub[r::d]
                    for a in range(len(grp) // 2):
                        if grp[a] != grp[-1 - a]:
                            changes += 1
                best = min(best, changes)
            return best

        # cost[i][j]: changes to make s[i..j] a semi-palindrome (INF if length 1)
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = semi_cost(s[i:j + 1])

        # dp[p][j]: min changes for first j chars split into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] < INF:
                        v = dp[p - 1][i] + cost[i][j - 1]
                        if v < dp[p][j]:
                            dp[p][j] = v
        return dp[k][n]
