# 49. Group Anagrams (Medium)

https://leetcode.com/problems/group-anagrams/

Given a list of strings, group the words that are anagrams of each other.

## Approach
1. Two words are anagrams if they have the same letters. Sorting the letters of each word gives the same string for all anagrams (`"eat"`, `"tea"`, `"ate"` -> `"aet"`).
2. Use that sorted string as a dictionary key; store the original words in a list under it.
3. Return all the lists.

## Complexity
- Time: O(n * k log k), n words of max length k.
- Space: O(n * k).
