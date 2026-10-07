class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string has valid parentheses
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # Queue for BFS and a set to avoid processing duplicate strings
        queue = {s}
        
        while queue:
            # Filter the current level for valid strings
            valid_strings = list(filter(isValid, queue))
            
            # If we found valid strings at this level, they have the minimum removals
            if valid_strings:
                return valid_strings
            
            # Generate the next level by removing one parenthesis at a time
            next_level = set()
            for current_str in queue:
                for i in range(len(current_str)):
                    # Only attempt removal if the character is a parenthesis
                    if current_str[i] in ('(', ')'):
                        new_str = current_str[:i] + current_str[i+1:]
                        next_level.add(new_str)
            
            queue = next_level
            
        return [""]
