# LeetCode 67 - Add Binary
# https://leetcode.com/problems/add-binary/
# Difficulty: Easy

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary strings and return the sum as a binary string.
        
        Approach: Simulate binary addition from right to left,
        tracking the carry bit.
        
        Time Complexity: O(max(m, n))
        Space Complexity: O(max(m, n))
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result.append(str(total % 2))
            carry = total // 2
        
        return ''.join(reversed(result))


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.addBinary("11", "1") == "100"
    assert sol.addBinary("1010", "1011") == "10101"
    assert sol.addBinary("0", "0") == "0"
    print("All test cases passed!")
