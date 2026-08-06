# LeetCode 3345 - Smallest Divisible Digit Product I
# https://leetcode.com/problems/smallest-divisible-digit-product-i/
# Difficulty: Easy

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        """
        Returns the smallest number greater than or equal to n such that
        the product of its digits is divisible by t.

        Approach:
        Since the digit product of a number containing '0' (like 100, 10) is 0,
        and 0 is divisible by any t (1 <= t <= 10), we will find a solution
        very quickly (within 10 increments). We can just iterate upwards from n.

        Time Complexity: O(log_10(n)) per check, which takes O(1) overall due to the small search space.
        Space Complexity: O(1)
        """
        curr = n
        while True:
            # Calculate product of digits
            prod = 1
            temp = curr
            while temp > 0:
                prod *= temp % 10
                temp //= 10
            
            if prod % t == 0:
                return curr
            curr += 1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.smallestNumber(10, 2) == 10
    assert sol.smallestNumber(15, 3) == 16
    print("All test cases passed!")
