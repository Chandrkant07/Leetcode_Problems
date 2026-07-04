# LeetCode 26 - Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(f"k = {k1}, nums = {nums1[:k1]}")  # k = 2, nums = [1, 2]
    
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(f"k = {k2}, nums = {nums2[:k2]}")  # k = 5, nums = [0, 1, 2, 3, 4]
