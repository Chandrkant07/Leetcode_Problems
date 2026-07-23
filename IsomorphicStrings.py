# LeetCode 205 - Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# Difficulty: Easy

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Check if two strings are isomorphic.
        Characters in s can be replaced to get t, preserving order.
        No two characters may map to the same character.
        
        Approach: Use two hash maps for bidirectional mapping.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for c1, c2 in zip(s, t):
            if c1 in s_to_t and s_to_t[c1] != c2:
                return False
            if c2 in t_to_s and t_to_s[c2] != c1:
                return False
            s_to_t[c1] = c2
            t_to_s[c2] = c1
        
        return True


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic("egg", "add") == True
    assert sol.isIsomorphic("foo", "bar") == False
    assert sol.isIsomorphic("paper", "title") == True
    assert sol.isIsomorphic("badc", "baba") == False
    print("All test cases passed!")
