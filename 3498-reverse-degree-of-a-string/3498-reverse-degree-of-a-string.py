class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        
        for i, char in enumerate(s):
            # 'a' maps to 26, 'b' to 25, ..., 'z' to 1
            reversed_val = 26 - (ord(char) - ord('a'))
            
            # Position in the string is 1-indexed
            position = i + 1
            
            total_degree += reversed_val * position
            
        return total_degree
