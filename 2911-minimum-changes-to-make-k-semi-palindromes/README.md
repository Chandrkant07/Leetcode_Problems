# 2911. Minimum Changes to Make K Semi-palindromes (Hard)

https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

Partition a string into `k` substrings so the total letter changes needed to make each a semi-palindrome is minimal.

## Approach
1. For every substring, compute the cost to make it a semi-palindrome: try each proper divisor `d` of its length, split into `d` strided groups, count mismatched mirror pairs in each group, and keep the minimum over `d`. Length-1 substrings have no valid divisor (cost = infinity).
2. DP over partitions: `dp[p][j]` = minimum cost to split the first `j` characters into `p` parts, `dp[p][j] = min(dp[p-1][i] + cost[i][j-1])`.
3. Answer is `dp[k][n]`.

## Complexity
- Time: O(n^3 * d(n)) worst case for the cost table (n = 200 is fine), plus O(k * n^2) for the DP.
- Space: O(n^2).
