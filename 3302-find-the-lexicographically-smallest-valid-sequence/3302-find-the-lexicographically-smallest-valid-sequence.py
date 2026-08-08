from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        """
        Finds the lexicographically smallest sequence of indices in word1
        such that the characters at these indices form a string that is
        almost equal (at most one character difference) to word2.

        Approach:
        1. Precompute an array `last` where `last[j]` is the rightmost index in word1
           that can match word2[j] when matching the suffix word2[j:] greedily from the right.
           If the suffix cannot be matched, `last[j]` is -1.
        2. Iterate through word2 from left to right (index j) and try to match it
           with the smallest possible index i in word1.
        3. If word1[i] == word2[j], we can match them greedily (no change used).
        4. If word1[i] != word2[j] and we haven't used our single allowed change yet,
           we can change word1[i] to word2[j] IF the remaining suffix word2[j+1:]
           can be matched in word1[i+1:] with 0 changes.
           This is true if j + 1 == len(word2) or last[j+1] > i.
        5. If we find a valid index for each character in word2, we return the sequence.
           Otherwise, return an empty list.

        Time Complexity: O(n + m) where n = len(word1) and m = len(word2).
        Space Complexity: O(m) for the `last` array and O(m) for the output sequence.
        """
        n = len(word1)
        m = len(word2)
        
        # Precompute rightmost greedy match for suffixes
        last = [-1] * m
        pos = n - 1
        for j in range(m - 1, -1, -1):
            while pos >= 0 and word1[pos] != word2[j]:
                pos -= 1
            if pos >= 0:
                last[j] = pos
                pos -= 1
            else:
                break
                
        seq = []
        changed = False
        i = 0
        j = 0
        
        while j < m:
            matched = False
            while i < n:
                if word1[i] == word2[j]:
                    seq.append(i)
                    i += 1
                    j += 1
                    matched = True
                    break
                elif not changed and (j + 1 == m or last[j + 1] > i):
                    seq.append(i)
                    changed = True
                    i += 1
                    j += 1
                    matched = True
                    break
                else:
                    i += 1
            if not matched:
                return []
                
        return seq