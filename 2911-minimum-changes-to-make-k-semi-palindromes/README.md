# 2911. Minimum Changes to Make K Semi-palindromes (Hard)

https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

Partition `s` into `k` substrings so that the total number of letter changes needed to turn every substring into a semi-palindrome is minimal.

## Approach
1. For every substring `s[i..j]` (length >= 2), compute the cheapest way to make it a semi-palindrome: try every proper divisor `d` of its length, split it into `d` interleaved groups, and count mismatched mirror pairs in each group. Take the minimum over `d`.
2. `dp[p][j]` = minimum changes for the first `j` characters split into `p` parts: `dp[p][j] = min over i of dp[p-1][i] + cost[i][j-1]`.
3. Answer is `dp[k][n]`.

## Complexity
- Time: O(n^3) for the cost table plus O(k * n^2) for the DP, fine for n <= 200.
- Space: O(n^2)
