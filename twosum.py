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

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))        # Output: [1, 2]
    print(sol.twoSum([3, 3], 6))           # Output: [0, 1]
