class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        k = 1  # numbers with at least 10^(3k) digits have at least k commas
        
        while 10 ** (3 * k) <= n:
            start = 10 ** (3 * k)
            ans += (n - start + 1) * k
            k += 1
        
        return ans