# 2243. Calculate Digit Sum of a String (Easy)

https://leetcode.com/problems/calculate-digit-sum-of-a-string/

Repeatedly split the digit string into groups of size `k`, replace each group by its digit sum, and join the results, until the string length is at most `k`.

## Approach
1. While `len(s) > k`, walk `s` in chunks of `k`.
2. Replace each chunk with the string of its digit sum and join them.
3. Return `s` once its length is `<= k`.

## Complexity
- Time: O(n) per round; the string shrinks each round, so the total is O(n) overall for the given limits.
- Space: O(n)
