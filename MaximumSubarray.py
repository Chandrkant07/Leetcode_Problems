# LeetCode 53 - Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Find the subarray with the largest sum.
        
        Approach: Kadane's Algorithm.
        Track current sum and max sum. Reset current sum
        when it drops below 0.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-1]) == -1
    print("All test cases passed!")
