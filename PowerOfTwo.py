# LeetCode 231 - Power of Two
# https://leetcode.com/problems/power-of-two/
# Difficulty: Easy

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Check if n is a power of two.
        
        Approach: A power of two in binary has exactly one '1' bit.
        n & (n - 1) clears the lowest set bit. If result is 0,
        n had only one set bit (power of two).
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return n > 0 and (n & (n - 1)) == 0


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.isPowerOfTwo(1) == True
    assert sol.isPowerOfTwo(16) == True
    assert sol.isPowerOfTwo(3) == False
    assert sol.isPowerOfTwo(0) == False
    assert sol.isPowerOfTwo(-4) == False
    print("All test cases passed!")
