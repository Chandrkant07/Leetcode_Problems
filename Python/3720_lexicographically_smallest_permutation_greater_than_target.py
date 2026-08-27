from collections import Counter


class Solution:
    def nextGreaterPermutation(self, s: str, target: str) -> str:
        """
        Return the lexicographically smallest permutation of `s`
        that is strictly greater than `target`.

        If no such permutation exists, return an empty string.
        """
        n = len(s)
        cnt = Counter(s)

        # Fast fail: if even the largest permutation is <= target, impossible.
        max_perm = ''.join(ch * cnt[ch] for ch in range(ord('z'), ord('a') - 1, -1))
        if max_perm <= target:
            return ""

        letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        # Can we complete remaining positions with current multiset
        # so that suffix is >= target[pos:] ?
        def can_be_ge(pos: int) -> bool:
            for i in range(pos, n):
                t = target[i]

                # Smallest available char
                smallest = None
                for c in letters:
                    if cnt[c] > 0:
                        smallest = c
                        break

                if smallest is None:
                    return True  # no positions left

                if smallest < t:
                    # To stay >= target, we'd need some char > t at this position.
                    has_greater = False
                    for c in letters[ord(t) - ord('a') + 1:]:
                        if cnt[c] > 0:
                            has_greater = True
                            break
                    if not has_greater:
                        return False
                    return True
                elif smallest > t:
                    # Already strictly greater possible.
                    return True
                else:
                    # smallest == t: forced to try equal here if possible
                    if cnt[t] == 0:
                        return False
                    cnt[t] -= 1
                    ok = can_be_ge(i + 1)
                    cnt[t] += 1
                    return ok
            return True

        ans = []
        tight = True  # prefix equal to target so far

        for i in range(n):
            start_idx = 0
            if tight:
                start_idx = ord(target[i]) - ord('a')

            placed = False
            for j in range(start_idx, 26):
                c = letters[j]
                if cnt[c] == 0:
                    continue

                if tight and c < target[i]:
                    continue

                cnt[c] -= 1

                if tight and c == target[i]:
                    # Must ensure we can still end up strictly greater later.
                    # If suffix can be >= target suffix, we can continue tight.
                    if can_be_ge(i + 1):
                        ans.append(c)
                        placed = True
                        break
                else:
                    # Becomes strictly greater here; fill rest minimally.
                    ans.append(c)
                    for k in range(26):
                        if cnt[letters[k]]:
                            ans.extend([letters[k]] * cnt[letters[k]])
                    return ''.join(ans)

                cnt[c] += 1

            if not placed:
                return ""

            # We only get here if we placed target[i] while tight.
            cnt[target[i]] -= 0  # no-op for clarity
            if ans[-1] != target[i]:
                tight = False

        # Constructed exact target; needs strictly greater.
        return "" if ''.join(ans) <= target else ''.join(ans)
