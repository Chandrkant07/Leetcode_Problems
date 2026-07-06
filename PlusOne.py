# LeetCode 66 - Plus One
# https://leetcode.com/problems/plus-one/
# Difficulty: Easy

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(sol.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
