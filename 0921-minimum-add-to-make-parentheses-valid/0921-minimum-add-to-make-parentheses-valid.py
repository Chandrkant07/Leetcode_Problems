class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0
        
        for char in s:
            if char == '(':
                # We expect a closing parenthesis later
                close_needed += 1
            else: # char == ')'
                if close_needed > 0:
                    # Match found! Reduce the expected closing parenthesis count
                    close_needed -= 1
                else:
                    # No matching '(' available, so we must manually add a '('
                    open_needed += 1
                    
        # The total insertions needed is the sum of unmatched open and close parentheses
        return open_needed + close_needed
