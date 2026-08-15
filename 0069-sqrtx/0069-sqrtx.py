class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            
            # Calculate mid_squared. Python handles large integers automatically.
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                # mid is a potential candidate, try searching for a larger one in the right half
                ans = mid
                left = mid + 1
            else: # mid_squared > x
                # mid is too large, search in the left half
                right = mid - 1
        
        return ans