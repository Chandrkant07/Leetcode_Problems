# LeetCode 66 - Plus One
# https://leetcode.com/problems/plus-one/
# Difficulty: Easy

# Given a large integer represented as an integer array digits,
# increment the large integer by one and return the resulting array.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Optimal approach: Traverse from the last digit.
        If digit < 9, increment and return immediately.
        If digit == 9, set to 0 and carry over to the next digit.
        If all digits are 9, prepend 1 to the result.

        Time Complexity: O(n)
        Space Complexity: O(1) in-place, O(n) only when all digits are 9
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

    def plusOneConversion(self, digits: list[int]) -> list[int]:
        """
        Alternative approach: Convert to integer, add one, convert back.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num = int("".join(map(str, digits))) + 1
        return [int(d) for d in str(num)]


# Example usage and test cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Normal increment
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4], "Test 1 Failed"

    # Test Case 2: No carry needed
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2], "Test 2 Failed"

    # Test Case 3: Single digit carry → new digit
    assert sol.plusOne([9]) == [1, 0], "Test 3 Failed"

    # Test Case 4: Multiple carries
    assert sol.plusOne([9, 9, 9]) == [1, 0, 0, 0], "Test 4 Failed"

    # Test Case 5: Carry propagates partially
    assert sol.plusOne([1, 9, 9]) == [2, 0, 0], "Test 5 Failed"

    # Test Case 6: Single digit, no carry
    assert sol.plusOne([0]) == [1], "Test 6 Failed"

    print("All test cases passed!")
