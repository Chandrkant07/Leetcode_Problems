from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        odd = [ch for ch, freq in cnt.items() if freq % 2]
        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""
        half = []
        for ch in sorted(cnt):
            half.extend([ch] * (cnt[ch] // 2))

        m = len(s) // 2
        prefix = target[:m]

        def build(left: str) -> str:
            return left + middle + left[::-1]

        def half_greater() -> str:
            # Find the lexicographically smallest half permutation > prefix.
            avail = Counter(half)
            left = []
            for i in range(m):
                start = ord(prefix[i]) - 96
                for x in range(start + 1, 27):
                    ch = chr(x + 96)
                    if avail[ch] > 0:
                        # Check if remaining chars can fill the suffix.
                        avail[ch] -= 1
                        suffix = []
                        for y in sorted(avail):
                            suffix.extend([y] * avail[y])
                        return build("".join(left) + ch + "".join(suffix))
                if avail[prefix[i]] == 0:
                    return ""
                left.append(prefix[i])
                avail[prefix[i]] -= 1
            return ""

        # First try any palindrome whose half is lexicographically greater than target half.
        ans = half_greater()
        if ans and ans > target:
            return ans

        # If the exact half matches target prefix, the full palindrome may still be greater.
        left = []
        avail = Counter(half)
        for ch in prefix:
            if avail[ch] == 0:
                break
            left.append(ch)
            avail[ch] -= 1
        else:
            cand = build("".join(left))
            if cand > target:
                return cand

        # General fallback: enumerate the lexicographically smallest valid half greater than prefix.
        # Build by trying to pivot from right to left.
        avail = Counter(half)
        for i in range(m - 1, -1, -1):
            ch = prefix[i]
            if avail[ch] == 0:
                # Consume the exact prefix path and continue.
                break
            avail[ch] -= 1
            for x in range(ord(ch) - 96 + 1, 27):
                nxt = chr(x + 96)
                if avail[nxt] > 0:
                    avail[nxt] -= 1
                    left = prefix[:i] + nxt
                    rest = []
                    for y in sorted(avail):
                        rest.extend([y] * avail[y])
                    return build(left + "".join(rest))
        return ""
