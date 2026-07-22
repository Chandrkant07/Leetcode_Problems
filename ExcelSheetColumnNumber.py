# LeetCode 171 - Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/
# Difficulty: Easy

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Convert Excel column title to its corresponding column number.
        A -> 1, B -> 2, ..., Z -> 26, AA -> 27, AB -> 28, ...
        
        Approach: Treat as base-26 number system.
        Process each character left to right, multiplying by 26.
        
        Time Complexity: O(n) where n is length of columnTitle
        Space Complexity: O(1)
        """
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.titleToNumber("A") == 1
    assert sol.titleToNumber("AB") == 28
    assert sol.titleToNumber("ZY") == 701
    assert sol.titleToNumber("Z") == 26
    print("All test cases passed!")
