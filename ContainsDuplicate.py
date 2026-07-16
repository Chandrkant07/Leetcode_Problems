# LeetCode 217 - Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Return True if any value appears at least twice in the array.
        
        Approach: Use a hash set to track seen numbers.
        If a number is already in the set, we found a duplicate.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) == True
    assert sol.containsDuplicate([1, 2, 3, 4]) == False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    print("All test cases passed!")
