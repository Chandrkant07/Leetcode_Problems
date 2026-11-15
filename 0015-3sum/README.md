# 15. 3Sum (Medium)

https://leetcode.com/problems/3sum/

Return all unique triplets in the array that sum to zero.

## Approach
1. Sort the array.
2. Fix the first element `nums[i]` (skipping duplicates), then use two pointers `l` and `r` on the remainder.
3. If the sum is below zero move `l` right, if above zero move `r` left; on a match record the triplet and skip duplicate values on both sides.
4. Stop early once `nums[i] > 0`.

## Complexity
- Time: O(n^2).
- Space: O(1) extra (ignoring output and sort).
