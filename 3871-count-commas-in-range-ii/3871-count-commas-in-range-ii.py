class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        threshold = 1000  # 10^3, start of 1-comma numbers
        
        while threshold <= n:
            ans += n - threshold + 1
            threshold *= 1000  # next level: 10^6, 10^9, ...
        
        return ans