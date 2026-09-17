class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1
        best = [INF] * (n + 1)

        left = 0
        window_sum = 0
        answer = INF

        for right, value in enumerate(arr):
            window_sum += value
            best[right + 1] = best[right]

            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            if window_sum == target:
                length = right - left + 1

                # Best subarray completely before the current one
                if best[left] != INF:
                    answer = min(answer, best[left] + length)

                # Store the shortest valid subarray seen so far
                best[right + 1] = min(best[right + 1], length)

        return -1 if answer == INF else answer