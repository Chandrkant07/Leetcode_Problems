# 3041. Maximize Consecutive Elements in an Array After Modification (Hard)

https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

Each element may be increased by at most 1. Pick the largest set of elements that, once sorted, form a run of consecutive integers.

## Approach
1. Sort the array.
2. `dp[v]` = longest consecutive run whose last value is `v`.
3. For each `x`, either raise it to `x+1` (extends a run ending at `x`) or keep it (extends a run ending at `x-1`). Update `dp[x+1]` first, then `dp[x]`, so one element is never used twice.
4. Answer is the maximum `dp` value.

## Complexity
- Time: O(n log n).
- Space: O(n).
