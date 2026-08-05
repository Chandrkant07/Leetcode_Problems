# LeetCode 3310 - Remove Methods From Project
# https://leetcode.com/problems/remove-methods-from-project/
# Difficulty: Medium

from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        """
        Finds all remaining methods after removing suspicious methods if possible.
        A method is suspicious if it is k or reachable from k.
        We can only remove them if no non-suspicious method invokes a suspicious one.

        Approach:
        1. Build an adjacency list representing the invocation graph.
        2. Perform a BFS starting from method k to identify all reachable (suspicious) methods.
        3. Check all invocations to ensure no non-suspicious method invokes a suspicious method.
        4. If the condition is met, return the non-suspicious methods. Otherwise, return all methods.

        Time Complexity: O(n + E) where E is the number of invocations.
        Space Complexity: O(n + E) to store the graph and the suspicious set.
        """
        # Step 1: Build the invocation graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        # Step 2: Find all suspicious methods (reachable from k) using BFS
        suspicious = {k}
        queue = [k]
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)

        # Step 3: Check if any invocation goes from a non-suspicious method to a suspicious one
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # If so, none of the suspicious methods can be removed
                return list(range(n))

        # Step 4: Otherwise, return all remaining (non-suspicious) methods
        return [i for i in range(n) if i not in suspicious]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.remainingMethods(4, 1, [[1, 2], [0, 1], [3, 2]])) == [0, 1, 2, 3]
    assert sorted(sol.remainingMethods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]])) == [3, 4]
    assert sorted(sol.remainingMethods(3, 2, [[1, 2], [0, 1], [2, 0]])) == []
    print("All test cases passed!")
