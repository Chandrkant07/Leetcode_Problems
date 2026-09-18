from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find the first and last occurrence of each character.
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Try to create the smallest valid substring
        # starting at each character's first occurrence.
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')

            if first[c] != i:
                continue

            left = i
            right = last[c]
            valid = True

            j = left
            while j <= right:
                curr = ord(s[j]) - ord('a')

                # An occurrence exists before the interval.
                if first[curr] < left:
                    valid = False
                    break

                right = max(right, last[curr])
                j += 1

            if valid:
                intervals.append((left, right))

        # Select non-overlapping intervals greedily by end position.
        intervals.sort(key=lambda interval: interval[1])

        answer = []
        previous_end = -1

        for left, right in intervals:
            if left > previous_end:
                answer.append(s[left:right + 1])
                previous_end = right

        return answer