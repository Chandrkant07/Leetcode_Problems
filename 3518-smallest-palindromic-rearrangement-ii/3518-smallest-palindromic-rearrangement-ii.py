from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = k

        # Count permutations of the remaining half
        def countWays(cnt):
            total = sum(cnt)
            ans = 1
            rem = total

            for x in cnt:
                if x == 0:
                    continue
                ans *= comb(rem, x)
                if ans >= LIMIT:
                    return LIMIT
                rem -= x
            return ans

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        halfCnt = [f // 2 for f in freq]

        mid = ""
        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + ord('a'))
                break

        if countWays(halfCnt) < k:
            return ""

        half = []
        halfLen = len(s) // 2

        for _ in range(halfLen):
            for c in range(26):
                if halfCnt[c] == 0:
                    continue

                halfCnt[c] -= 1
                ways = countWays(halfCnt)

                if ways >= k:
                    half.append(chr(c + ord('a')))
                    break

                k -= ways
                halfCnt[c] += 1

        left = "".join(half)
        return left + mid + left[::-1]