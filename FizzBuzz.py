# LeetCode 412 - Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/
# Difficulty: Easy

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(3))   # Output: ["1", "2", "Fizz"]
    print(sol.fizzBuzz(5))   # Output: ["1", "2", "Fizz", "4", "Buzz"]
    print(sol.fizzBuzz(15))  # Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
