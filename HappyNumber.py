# LeetCode 202 - Happy Number
# https://leetcode.com/problems/happy-number/
# Difficulty: Easy

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if a number is 'happy'.
        
        A happy number is defined by replacing the number by the sum
        of the squares of its digits, repeating until the number
        equals 1 or loops endlessly in a cycle.
        
        Approach: Floyd's cycle detection (slow/fast pointers).
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        def get_next(number):
            total = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total += digit ** 2
            return total
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(19) == True
    assert sol.isHappy(2) == False
    assert sol.isHappy(1) == True
    print("All test cases passed!")
