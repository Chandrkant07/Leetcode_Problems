class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until matching '(' is found
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                # Remove the '(' from the stack
                if stack:
                    stack.pop()
                
                # Push the reversed substring back into the stack
                # Since temp already popped elements in reverse order,
                # appending them directly reverses the content.
                stack.extend(temp)
            else:
                # Push lower case letters and '(' to the stack
                stack.append(char)
                
        return "".join(stack)
