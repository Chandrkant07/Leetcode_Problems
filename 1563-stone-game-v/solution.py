from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # Base case: if only one stone, score is 0.
        if n == 1:
            return 0

        # Calculate prefix sums to get subarray sums efficiently
        # prefix_sum[p] stores the sum of stoneValue[0...p-1]
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

        # dp[i][j] stores the maximum score Alice can get from stoneValue[i...j]
        # Initialize with 0s (dp[i][i] is naturally 0 as per base case)
        dp = [[0] * n for _ in range(n)]

        # Iterate over the length of the subarray (from 2 up to n)
        for length in range(2, n + 1):
            # Iterate over the starting index i
            for i in range(n - length + 1):
                j = i + length - 1  # Calculate the corresponding ending index j
                
                max_score_for_current_segment = 0
                
                # Alice tries all possible split points k
                # k divides [i...j] into [i...k] and [k+1...j]
                for k in range(i, j):
                    sum_left = prefix_sum[k + 1] - prefix_sum[i]
                    sum_right = prefix_sum[j + 1] - prefix_sum[k + 1]

                    current_split_score = 0
                    if sum_left < sum_right:
                        # Bob discards the right row; Alice gets sum_left and plays on the left part
                        current_split_score = sum_left + dp[i][k]
                    elif sum_right < sum_left:
                        # Bob discards the left row; Alice gets sum_right and plays on the right part
                        current_split_score = sum_right + dp[k + 1][j]
                    else: # sum_left == sum_right
                        # Alice chooses to keep the part that maximizes her future score
                        current_split_score = sum_left + max(dp[i][k], dp[k + 1][j])
                    
                    # Alice picks the split k that yields the maximum score
                    max_score_for_current_segment = max(max_score_for_current_segment, current_split_score)
                
                dp[i][j] = max_score_for_current_segment
        
        # The final answer is the maximum score Alice can get from the entire array
        return dp[0][n - 1]
