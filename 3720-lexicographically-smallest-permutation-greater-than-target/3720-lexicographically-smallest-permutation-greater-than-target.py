from functools import lru_cache

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # quick impossible check: max permutation <= target
        max_perm = ''.join(chr(i + 97) * cnt[i] for i in range(25, -1, -1))
        if max_perm <= target:
            return ""

        @lru_cache(None)
        def can_build_ge(pos: int, tight: int, state: tuple) -> bool:
            if pos == n:
                return True

            arr = list(state)
            t = ord(target[pos]) - 97 if tight else 0

            for c in range(t, 26):
                if arr[c] == 0:
                    continue
                arr[c] -= 1
                ntight = 1 if (tight and c == t) else 0
                if can_build_ge(pos + 1, ntight, tuple(arr)):
                    return True
                arr[c] += 1
            return False

        # Build smallest permutation >= target
        ans = []
        tight = 1
        for pos in range(n):
            t = ord(target[pos]) - 97 if tight else 0
            for c in range(t, 26):
                if cnt[c] == 0:
                    continue
                cnt[c] -= 1
                ntight = 1 if (tight and c == t) else 0
                if can_build_ge(pos + 1, ntight, tuple(cnt)):
                    ans.append(chr(c + 97))
                    tight = ntight
                    break
                cnt[c] += 1
            else:
                return ""

        cand = ''.join(ans)
        if cand > target:
            return cand

        # cand == target -> next permutation
        arr = list(cand)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i < 0:
            return ""
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])
        return ''.join(arr)