# LeetCode 344 - Reverse String
# https://leetcode.com/problems/reverse-string/
# Difficulty: Easy

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example usage
if __name__ == "__main__":
    sol = Solution()
    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    print(s1)  # Output: ["o", "l", "l", "e", "h"]
    
    s2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s2)
    print(s2)  # Output: ["h", "a", "n", "n", "a", "H"]
