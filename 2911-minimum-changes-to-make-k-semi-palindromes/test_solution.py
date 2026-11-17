from itertools import combinations

from solution import Solution


def is_semi(t):
    m = len(t)
    for d in range(1, m):
        if m % d == 0 and all(t[r::d] == t[r::d][::-1] for r in range(d)):
            return True
    return False


def min_changes_to_semi(t):
    # brute force over all strings over the letters used + one extra
    from itertools import product
    letters = sorted(set(t)) + ["z"]
    best = len(t)
    for cand in product(letters, repeat=len(t)):
        c = "".join(cand)
        if is_semi(c):
            best = min(best, sum(a != b for a, b in zip(t, c)))
    return best


def brute(s, k):
    n = len(s)
    best = float("inf")
    for cuts in combinations(range(1, n), k - 1):
        b = [0, *cuts, n]
        parts = [s[b[i]:b[i + 1]] for i in range(k)]
        if any(len(p) < 2 for p in parts):
            continue
        best = min(best, sum(min_changes_to_semi(p) for p in parts))
    return best


def test_examples():
    s = Solution()
    assert s.minimumChanges("abcac", 2) == 1
    assert s.minimumChanges("abcdef", 2) == 2
    assert s.minimumChanges("aabbaa", 3) == 0


def test_minimum_length():
    assert Solution().minimumChanges("ab", 1) == 1
    assert Solution().minimumChanges("aa", 1) == 0


def test_matches_bruteforce():
    s = Solution()
    for word, k in [("abcab", 1), ("abcdab", 2), ("abbcde", 3), ("aabcda", 2)]:
        assert s.minimumChanges(word, k) == brute(word, k), (word, k)


def test_max_size_runs():
    import string
    word = (string.ascii_lowercase * 8)[:200]
    assert Solution().minimumChanges(word, 5) >= 0
