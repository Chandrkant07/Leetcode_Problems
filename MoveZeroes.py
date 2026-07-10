# LeetCode 283 - Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)  # Output: [1, 3, 12, 0, 0]
    
    nums2 = [0]
    sol.moveZeroes(nums2)
    print(nums2)  # Output: [0]
