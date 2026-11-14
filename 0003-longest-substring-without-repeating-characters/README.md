# 3. Longest Substring Without Repeating Characters (Medium)

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string `s`, find the length of the longest substring without repeating characters.

## Approach
1. Sliding window `[left, right]` that never contains a duplicate character.
2. Keep a dictionary of the last index where each character was seen.
3. When the current character was last seen inside the window, move `left` to just after that index.
4. Track the maximum window length.

## Complexity
- Time: O(n).
- Space: O(min(n, alphabet size)).
