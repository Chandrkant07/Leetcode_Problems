class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Find the first closing brace '}'
        j = expression.find('}')
        if j == -1:
            return [expression]
        
        # Find the last opening brace '{' before this '}'
        i = expression.rfind('{', 0, j)
        
        # Split into parts: left, inside the braces, and right
        left = expression[:i]
        right = expression[j+1:]
        mid = expression[i+1:j].split(',')
        
        # Generate combinations for each comma-separated option inside the innermost braces
        ans = set()
        for m in mid:
            ans |= set(self.braceExpansionII(left + m + right))
            
        return sorted(list(ans))
