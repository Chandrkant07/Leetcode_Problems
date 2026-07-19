# LeetCode 268 - Missing Number
# https://leetcode.com/problems/missing-number/
# Difficulty: Easy

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Find the missing number in range [0, n].
        
        Approach: Use Gauss formula. Sum of 0..n is n*(n+1)/2.
        Subtract actual sum to find missing number.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.missingNumber([3, 0, 1]) == 2
    assert sol.missingNumber([0, 1]) == 2
    assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All test cases passed!")
