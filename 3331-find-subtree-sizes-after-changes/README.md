# 3331. Find Subtree Sizes After Changes (Medium)

https://leetcode.com/problems/find-subtree-sizes-after-changes/

Given a tree rooted at 0 (`parent`) and a character per node (`s`), each node `x` is re-attached to its closest ancestor `y` with `s[y] == s[x]` (if any). Return the subtree sizes of the new tree.

## Approach
1. DFS from the root keeping, for each letter, the closest ancestor on the current path (restored on exit). The first match for a node's letter is its new parent.
2. All re-attachments are decided on the original tree, so compute them first, then build the new tree.
3. Traverse the new tree, then accumulate subtree sizes from leaves up in reverse visit order.
Iterative DFS avoids recursion limits.

## Complexity
- Time: O(n)
- Space: O(n)
