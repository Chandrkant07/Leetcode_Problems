class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            r = num % k
            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[r] += 1

            # Extend all subarrays ending at previous position
            for rem in range(k):
                new_rem = (rem * r) % k
                new_dp[new_rem] += dp[rem]

            # All subarrays ending here contribute to the answer
            for rem in range(k):
                ans[rem] += new_dp[rem]

            dp = new_dp

        return ans