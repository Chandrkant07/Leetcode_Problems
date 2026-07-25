# LeetCode 141 - Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if a linked list has a cycle.
        
        Approach: Floyd's Tortoise and Hare algorithm.
        Use two pointers - slow moves 1 step, fast moves 2 steps.
        If they meet, there's a cycle.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Cycle exists
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle
    assert sol.hasCycle(node1) == True
    
    # Test 2: No cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert sol.hasCycle(node1) == False
    
    # Test 3: Empty list
    assert sol.hasCycle(None) == False
    
    print("All test cases passed!")
