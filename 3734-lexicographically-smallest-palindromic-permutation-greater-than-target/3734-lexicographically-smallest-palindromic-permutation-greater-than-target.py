class Solution:
    def smallestPalindrome(self, s: str, target: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        odd_count = 0
        mid = ""
        for i in range(26):
            if freq[i] % 2:
                odd_count += 1
                mid = chr(i + ord('a'))
                if odd_count > 1:
                    return ""

        half_counts = [x // 2 for x in freq]
        half_len = len(s) // 2
        left_target = target[:half_len]

        def max_half_string(cnt):
            return "".join(chr(i + ord('a')) * cnt[i] for i in range(25, -1, -1))

        def build_smallest_ge(bound):
            cnt = half_counts[:]
            ans = []
            tight = True

            for i in range(half_len):
                lower = ord(bound[i]) - ord('a') if tight else 0
                chosen = -1

                for c in range(lower, 26):
                    if cnt[c] == 0:
                        continue

                    if not tight or c > lower:
                        chosen = c
                        break

                    cnt[c] -= 1
                    if max_half_string(cnt) >= bound[i + 1:]:
                        chosen = c
                        cnt[c] += 1
                        break
                    cnt[c] += 1

                if chosen == -1:
                    return None

                cnt[chosen] -= 1
                ans.append(chr(chosen + ord('a')))
                if tight and chosen > lower:
                    tight = False

            return "".join(ans)

        def build_smallest_gt(bound):
            cnt = half_counts[:]
            ans = []
            greater = False

            for i in range(half_len):
                lower = ord(bound[i]) - ord('a') if not greater else 0
                chosen = -1

                for c in range(lower, 26):
                    if cnt[c] == 0:
                        continue

                    if greater or c > lower:
                        chosen = c
                        break

                    cnt[c] -= 1
                    if max_half_string(cnt) > bound[i + 1:]:
                        chosen = c
                        cnt[c] += 1
                        break
                    cnt[c] += 1

                if chosen == -1:
                    return None

                cnt[chosen] -= 1
                ans.append(chr(chosen + ord('a')))
                if not greater and chosen > lower:
                    greater = True

            return "".join(ans) if greater else None

        left = build_smallest_ge(left_target)
        if left is None:
            return ""

        palindrome = left + mid + left[::-1]
        if palindrome > target:
            return palindrome

        left = build_smallest_gt(left)
        if left is None:
            return ""

        return left + mid + left[::-1]
