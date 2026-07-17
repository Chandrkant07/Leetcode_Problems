# LeetCode 350 - Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Difficulty: Easy

from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Find the intersection of two arrays (including duplicates).
        
        Approach: Use Counter to count frequencies in nums1,
        then iterate nums2 and collect common elements.
        
        Time Complexity: O(m + n)
        Space Complexity: O(min(m, n))
        """
        counts = Counter(nums1)
        result = []
        
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
    assert sorted(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert sol.intersect([1, 2, 3], [4, 5, 6]) == []
    print("All test cases passed!")
