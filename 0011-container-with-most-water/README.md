# 11. Container With Most Water (Medium)

https://leetcode.com/problems/container-with-most-water/

Given an array `height`, pick two lines that together with the x-axis form a container holding the most water.

## Approach
1. Start with two pointers at both ends; the area is `min(height[l], height[r]) * (r - l)`.
2. Moving the taller line inward can never help (width shrinks, height is still capped by the shorter line), so always move the pointer at the shorter line.
3. Track the maximum area seen until the pointers meet.

## Complexity
- Time: O(n).
- Space: O(1).
