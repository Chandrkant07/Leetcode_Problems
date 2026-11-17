import itertools
import pytest
from solution import Solution


def brute(s, k):
    n = len(s)

    def semi(sub):
        m = len(sub)
        best = None
        for d in range(1, m):
            if m % d:
                continue
            c = 0
            for r in range(d):
                g = sub[r::d]
                c += sum(g[a] != g[-1 - a] for a in range(len(g) // 2))
            best = c if best is None else min(best, c)
        return best

    res = None
    for cuts in itertools.combinations(range(1, n), k - 1):
        b = [0, *cuts, n]
        tot = 0
        for x, y in zip(b, b[1:]):
            c = semi(s[x:y])
            if c is None:
                tot = None
                break
            tot += c
        if tot is not None and (res is None or tot < res):
            res = tot
    return res


@pytest.mark.parametrize("s,k,exp", [
    ("abcac", 2, 1),
    ("abcdef", 2, 2),
    ("aabbaa", 3, 0),
    ("aa", 1, 0),
    ("ab", 1, 1),
])
def test_examples(s, k, exp):
    assert Solution().minimumChanges(s, k) == exp


def test_against_brute():
    import random
    random.seed(1)
    for _ in range(60):
        n = random.randint(2, 10)
        s = "".join(random.choice("abc") for _ in range(n))
        k = random.randint(1, n // 2)
        assert Solution().minimumChanges(s, k) == brute(s, k)


def test_max_size_runs():
    s = "abcde" * 40
    assert isinstance(Solution().minimumChanges(s, 10), int)
