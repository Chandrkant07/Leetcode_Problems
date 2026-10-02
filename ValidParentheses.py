class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their matching opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it is a closing bracket
            if char in mapping:
                # Pop the top element from stack if it is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapped opening bracket doesn't match the stack's top
                if mapping[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it to the stack
                stack.append(char)
                
        # If stack is empty, all brackets matched correctly
        return not stack
