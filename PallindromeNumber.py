# LeetCode 9 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return original == reversed_num

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # Output: True
    print(sol.isPalindrome(-121))  # Output: False
    print(sol.isPalindrome(10))    # Output: False
