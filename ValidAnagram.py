# LeetCode 242 - Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # Output: True
    print(sol.isAnagram("rat", "car"))          # Output: False
