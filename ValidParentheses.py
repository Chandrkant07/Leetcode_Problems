# LeetCode 20 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))       # Output: True
    print(sol.isValid("()[]{}"))   # Output: True
    print(sol.isValid("(]"))       # Output: False
