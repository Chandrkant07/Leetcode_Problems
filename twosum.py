# LeetCode 1 - Two Sum
# https://leetcode.com/problems/two-sum/
# Difficulty: Easy

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []
