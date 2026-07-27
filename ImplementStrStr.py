# LeetCode 28 - Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find first occurrence of needle in haystack.
        
        Approach: Sliding window comparison.
        Check each substring of haystack with length of needle.
        
        Time Complexity: O(n * m) where n = len(haystack), m = len(needle)
        Space Complexity: O(1)
        """
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        
        return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("sadbutsad", "sad") == 0
    assert sol.strStr("leetcode", "leeto") == -1
    assert sol.strStr("hello", "ll") == 2
    assert sol.strStr("a", "a") == 0
    print("All test cases passed!")
