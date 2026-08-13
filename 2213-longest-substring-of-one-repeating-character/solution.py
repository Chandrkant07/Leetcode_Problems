"""
2213. Longest Substring of One Repeating Character (Hard)

Approach: Segment Tree with merge
- Each segment tree node stores:
  - pref: length of longest prefix of same char
  - suf: length of longest suffix of same char  
  - best: longest substring of one repeating char in range
  - lc/rc: leftmost and rightmost characters
  - length: segment length
- Point update: change a character, rebuild ancestors
- Query: root's 'best' gives the global answer

Time:  O((n + k) log n) — build O(n log n), each query O(log n)
Space: O(n)
"""

from typing import List


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)

        # Segment tree arrays (1-indexed, size 4*n)
        pref = [0] * (4 * n)
        suf = [0] * (4 * n)
        best = [0] * (4 * n)
        lc = [''] * (4 * n)
        rc = [''] * (4 * n)
        ln = [0] * (4 * n)  # segment length

        def push_up(node):
            l, r = 2 * node, 2 * node + 1
            ln[node] = ln[l] + ln[r]
            lc[node] = lc[l]
            rc[node] = rc[r]
            pref[node] = pref[l]
            suf[node] = suf[r]
            best[node] = max(best[l], best[r])

            # Merge: if right char of left child == left char of right child
            if rc[l] == lc[r]:
                merged = suf[l] + pref[r]
                best[node] = max(best[node], merged)
                # Extend prefix if entire left child is one char
                if pref[l] == ln[l]:
                    pref[node] = pref[l] + pref[r]
                # Extend suffix if entire right child is one char
                if suf[r] == ln[r]:
                    suf[node] = suf[r] + suf[l]

        def build(node, lo, hi):
            if lo == hi:
                pref[node] = suf[node] = best[node] = 1
                lc[node] = rc[node] = arr[lo]
                ln[node] = 1
                return
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            push_up(node)

        def update(node, lo, hi, idx, ch):
            if lo == hi:
                arr[idx] = ch
                lc[node] = rc[node] = ch
                return
            mid = (lo + hi) // 2
            if idx <= mid:
                update(2 * node, lo, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, hi, idx, ch)
            push_up(node)

        build(1, 0, n - 1)

        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            res.append(best[1])

        return res
