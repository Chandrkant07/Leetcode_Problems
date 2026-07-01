# LeetCode 13 - Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))     # Output: 3
    print(sol.romanToInt("LVIII"))   # Output: 58
    print(sol.romanToInt("MCMXCIV")) # Output: 1994
