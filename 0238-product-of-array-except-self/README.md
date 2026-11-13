# 238. Product of Array Except Self (Medium)

https://leetcode.com/problems/product-of-array-except-self/

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of all elements of `nums` except `nums[i]`, without using division and in O(n) time.

## Approach
1. The answer at index `i` is (product of everything left of `i`) * (product of everything right of `i`).
2. First pass left to right: store the running prefix product in `res[i]`.
3. Second pass right to left: multiply `res[i]` by the running suffix product.
4. No division is needed, so zeros are handled naturally.

## Complexity
- Time: O(n).
- Space: O(1) extra (excluding the output array).
