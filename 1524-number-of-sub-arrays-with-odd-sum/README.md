# 1524. Number of Sub-arrays With Odd Sum (Medium)

https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Count the sub-arrays of `arr` whose sum is odd, modulo 10^9 + 7.

## Approach
1. A sub-array sum is `prefix[j] - prefix[i]`, which is odd exactly when the two prefix sums have different parity.
2. Track the parity of the running prefix and how many earlier prefixes (including the empty one) were odd or even.
3. If the current prefix is odd, add the count of even prefixes; otherwise add the count of odd prefixes.

## Complexity
- Time: O(n)
- Space: O(1)
