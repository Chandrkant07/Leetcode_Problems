# LeetCode 70 - Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))   # Output: 2
    print(sol.climbStairs(3))   # Output: 3
    print(sol.climbStairs(5))   # Output: 8
