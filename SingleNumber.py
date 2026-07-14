# LeetCode 136 - Single Number
# https://leetcode.com/problems/single-number/
# Difficulty: Easy

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Find the element that appears only once.
        Every other element appears exactly twice.
        
        Approach: XOR all numbers. Since a ^ a = 0 and a ^ 0 = a,
        all pairs cancel out, leaving the single number.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        for num in nums:
            result ^= num
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([2, 2, 1]) == 1
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sol.singleNumber([1]) == 1
    print("All test cases passed!")
