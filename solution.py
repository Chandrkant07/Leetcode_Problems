from bisect import bisect_left
from typing import List, Tuple

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # (l, r, w, original_index)
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: (x[1], x[0], x[3]))  # sort by end
        
        starts = [x[0] for x in arr]
        ends = [x[1] for x in arr]
        weights = [x[2] for x in arr]
        orig = [x[3] for x in arr]
        
        # p[i]: largest j < i with ends[j] < starts[i]
        p = []
        for i in range(n):
            j = bisect_left(ends, starts[i]) - 1   # first end >= start => j before it
            p.append(j)
        
        NEG = -10**30
        
        # dp[i][k] => best using first i intervals (0..i-1), picking exactly k
        # store tuple (weight_sum, tuple_of_indices_sorted)
        dp = [[(NEG, ()) for _ in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, ())
        
        def better(a: Tuple[int, Tuple[int, ...]], b: Tuple[int, Tuple[int, ...]]) -> bool:
            # True if a is better than b
            if a[0] != b[0]:
                return a[0] > b[0]
            return a[1] < b[1]   # lexicographically smaller
        
        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]
            
            # skip
            for k in range(5):
                dp[i][k] = dp[i - 1][k]
            
            # take
            prev_i = p[i - 1] + 1  # convert interval index to dp row
            for k in range(1, 5):
                prev_w, prev_list = dp[prev_i][k - 1]
                if prev_w == NEG:
                    continue
                cand_w = prev_w + w
                # Keep output list sorted by original index for lexicographic comparison/output
                cand_list = tuple(sorted(prev_list + (idx,)))
                cand = (cand_w, cand_list)
                
                if better(cand, dp[i][k]):
                    dp[i][k] = cand
        
        # up to 4 intervals => choose best among k=0..4
        ans = dp[n][0]
        for k in range(1, 5):
            if better(dp[n][k], ans):
                ans = dp[n][k]
        
        return list(ans[1])
