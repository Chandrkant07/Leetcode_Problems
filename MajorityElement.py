# LeetCode 169 - Majority Element
# https://leetcode.com/problems/majority-element/
# Difficulty: Easy

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Find the majority element (appears more than n/2 times).
        
        Approach: Boyer-Moore Voting Algorithm.
        Maintain a candidate and count. If count drops to 0,
        switch candidate to current element.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        candidate = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([3, 2, 3]) == 3
    assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert sol.majorityElement([1]) == 1
    print("All test cases passed!")
