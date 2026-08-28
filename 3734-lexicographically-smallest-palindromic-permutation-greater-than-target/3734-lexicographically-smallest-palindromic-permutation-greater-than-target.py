from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        n = len(s)

        # Check palindrome possibility
        odd = [c for c in cnt if cnt[c] % 2 == 1]
        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""
        m = n // 2

        # Available characters for the left half
        half_cnt = [0] * 26
        for c in cnt:
            half_cnt[ord(c) - ord('a')] = cnt[c] // 2

        prefix = target[:m]

        def build(left):
            left = "".join(left)
            return left + middle + left[::-1]

        # Try to make left half exactly equal to target's first half
        available = half_cnt[:]
        left = []
        possible = True

        for ch in prefix:
            x = ord(ch) - ord('a')
            if available[x] == 0:
                possible = False
                break
            available[x] -= 1
            left.append(ch)

        if possible:
            candidate = build(left)
            if candidate > target:
                return candidate

        # Find the smallest permutation of the half
        # that is lexicographically greater than target[:m]
        available = half_cnt[:]

        # Match prefix and store remaining counts at every position
        states = []
        valid_prefix = True

        for i, ch in enumerate(prefix):
            states.append(available[:])
            x = ord(ch) - ord('a')

            if available[x] == 0:
                valid_prefix = False
                break

            available[x] -= 1

        # Try changing from right to left
        for i in range(m - 1, -1, -1):
            available = half_cnt[:]

            # Use target prefix before position i
            ok = True
            left = []

            for j in range(i):
                x = ord(prefix[j]) - ord('a')

                if available[x] == 0:
                    ok = False
                    break

                available[x] -= 1
                left.append(prefix[j])

            if not ok:
                continue

            # Choose smallest character greater than prefix[i]
            current = ord(prefix[i]) - ord('a')
            chosen = -1

            for x in range(current + 1, 26):
                if available[x] > 0:
                    chosen = x
                    break

            if chosen == -1:
                continue

            left.append(chr(chosen + ord('a')))
            available[chosen] -= 1

            # Add remaining characters in sorted order
            for x in range(26):
                left.extend([chr(x + ord('a'))] * available[x])

            return build(left)

        return ""