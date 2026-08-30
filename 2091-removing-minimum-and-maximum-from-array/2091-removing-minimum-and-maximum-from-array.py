class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Remove both from front
        option1 = right + 1

        # Remove both from back
        option2 = n - left

        # Remove one from front and one from back
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)