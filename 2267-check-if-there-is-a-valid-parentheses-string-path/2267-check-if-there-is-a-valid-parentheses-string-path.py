class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
            
        memo = {}
        
        def dfs(r, c, balance):
            # Update balance based on current cell value
            balance += 1 if grid[r][c] == '(' else -1
            
            # If closed parentheses exceed open ones, this path is invalid
            if balance < 0:
                return False
                
            # If we reached the bottom-right corner, check if it's perfectly balanced
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            state = (r, c, balance)
            if state in memo:
                return memo[state]
                
            # Explore moving right and moving down
            res = False
            if c + 1 < n:
                res = res or dfs(r, c + 1, balance)
            if r + 1 < m:
                res = res or dfs(r + 1, c, balance)
                
            memo[state] = res
            return res

        return dfs(0, 0, 0)
