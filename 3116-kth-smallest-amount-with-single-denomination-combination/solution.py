import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant coins (coins that are multiples of another coin in the list)
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % d == 0 for d in filtered_coins):
                filtered_coins.append(c)
        
        coins = filtered_coins
        n = len(coins)
        
        # Precompute subset LCMs and sign for inclusion-exclusion principle
        subsets = []
        for mask in range(1, 1 << n):
            cnt = 0
            lcm_val = 1
            for i in range(n):
                if (mask >> i) & 1:
                    cnt += 1
                    lcm_val = math.lcm(lcm_val, coins[i])
            sign = 1 if (cnt % 2 == 1) else -1
            subsets.append((lcm_val, sign))
        
        def count_multiples(X: int) -> int:
            res = 0
            for lcm_val, sign in subsets:
                res += sign * (X // lcm_val)
            return res
        
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
