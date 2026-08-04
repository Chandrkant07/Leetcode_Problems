# LeetCode 3731 - Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/
# Difficulty: Easy

class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        """
        Find all missing integers in the range defined by min(nums) and max(nums).
        
        Approach: Use a set for O(1) lookups. Find the range [min_val, max_val].
        Iterate through the range and check if each number is present in the set.
        
        Time Complexity: O(n + range_size) where range_size = max(nums) - min(nums) + 1.
                         Since constraints state nums[i] <= 100, range_size <= 100,
                         making this O(n) in practice.
        Space Complexity: O(n) for the lookup set.
        """
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        missing = []
        for val in range(min_val, max_val + 1):
            if val not in num_set:
                missing.append(val)
                
        return missing


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.findMissingElements([1, 4, 2, 5]) == [3]
    assert sol.findMissingElements([7, 8, 6, 9]) == []
    assert sol.findMissingElements([5, 1]) == [2, 3, 4]
    print("All test cases passed!")
