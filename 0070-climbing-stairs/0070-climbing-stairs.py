class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # dp[i] represents the number of ways to reach step i
        # We only need the previous two values, so we can optimize space
        # Initialize for n=1 and n=2
        one_step_before = 2 # Represents dp[2]
        two_steps_before = 1 # Represents dp[1]
        
        # Start from n=3 up to the given n
        for i in range(3, n + 1):
            current_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current_ways
            
        return one_step_before # This will hold dp[n]