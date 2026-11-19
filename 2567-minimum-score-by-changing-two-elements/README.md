# 2567. Minimum Score by Changing Two Elements (Medium)

https://leetcode.com/problems/minimum-score-by-changing-two-elements/

Change two elements of `nums` to any values so that (max difference + min difference) is minimized.

## Approach
1. Changing two elements to equal an existing value makes the low score 0, so only the high score (max - min) matters.
2. Sort the array. The best choice is to change the two elements that shrink the range most: the two smallest, the two largest, or the smallest and the largest.
3. Answer = min(`a[n-1]-a[2]`, `a[n-2]-a[1]`, `a[n-3]-a[0]`).

## Complexity
- Time: O(n log n) for sorting.
- Space: O(1) extra (in-place sort).
