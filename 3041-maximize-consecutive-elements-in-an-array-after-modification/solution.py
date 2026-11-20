from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        best = 0
        for x in nums:
            up = dp.get(x, 0) + 1        # x -> x+1, extends a run ending at x
            same = dp.get(x - 1, 0) + 1  # x stays, extends a run ending at x-1
            dp[x + 1] = max(dp.get(x + 1, 0), up)
            dp[x] = max(dp.get(x, 0), same)
            best = max(best, dp[x + 1], dp[x])
        return best
