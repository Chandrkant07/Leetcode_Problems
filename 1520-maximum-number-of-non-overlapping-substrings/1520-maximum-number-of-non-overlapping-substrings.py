from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            first[index] = min(first[index], i)
            last[index] = i

        intervals = []

        # A valid substring must start at a character's first occurrence.
        for left, ch in enumerate(s):
            index = ord(ch) - ord('a')
            if first[index] != left:
                continue

            right = last[index]
            valid = True
            position = left

            while position <= right:
                current = ord(s[position]) - ord('a')
                if first[current] < left:
                    valid = False
                    break

                right = max(right, last[current])
                position += 1

            if valid:
                intervals.append((left, right))

        # Earliest finishing intervals maximize the number of substrings.
        intervals.sort(key=lambda interval: interval[1])

        answer = []
        previous_end = -1

        for left, right in intervals:
            if left > previous_end:
                answer.append(s[left:right + 1])
                previous_end = right

        return answer
