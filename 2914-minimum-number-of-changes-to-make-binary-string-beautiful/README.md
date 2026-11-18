# 2914. Minimum Number of Changes to Make Binary String Beautiful (Medium)

https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

Given an even-length binary string, find the minimum number of character flips so it can be split into substrings of even length that each contain only 0s or only 1s.

## Approach
1. A string is beautiful iff it can be cut into equal-character blocks of even length. Every such block splits into pairs of equal characters, and conversely if every aligned pair (indices 2i, 2i+1) is equal, the runs all have even length.
2. So each aligned pair must match. Each mismatched pair costs exactly one flip, and pairs are independent.
3. Count mismatched pairs.

## Complexity
- Time: O(n).
- Space: O(1).
