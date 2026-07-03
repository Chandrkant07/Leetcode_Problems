# LeetCode 21 - Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next

# Example usage
if __name__ == "__main__":
    sol = Solution()
    # Create list1: 1 -> 2 -> 4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    # Create list2: 1 -> 3 -> 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    result = sol.mergeTwoLists(l1, l2)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
