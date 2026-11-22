# 2124. Check if All A's Appears Before All B's (Easy)

https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

Given a string `s` of only `'a'` and `'b'`, return true if every `'a'` appears before every `'b'`.

## Approach
1. Every `'a'` is before every `'b'` exactly when the string has the form `a...ab...b`.
2. That is violated only if some `'b'` is immediately followed by an `'a'`, so it is enough to check that `"ba"` is not a substring.

## Complexity
- Time: O(n).
- Space: O(1).
