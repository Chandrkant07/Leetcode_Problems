from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        arr = sorted((nums[i], i) for i in range(n))
        result = nums[:]
        i = 0

        while i < n:
            j = i
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            values = [arr[k][0] for k in range(i, j + 1)]
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            for k in range(len(indices)):
                result[indices[k]] = values[k]

            i = j + 1

        return result
