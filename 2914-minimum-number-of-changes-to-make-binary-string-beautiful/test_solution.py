import pytest
from solution import Solution


@pytest.mark.parametrize("s,expected", [
    ("1001", 2),
    ("10", 1),
    ("0000", 0),
    ("11", 0),
    ("01", 1),
    ("0101", 2),
    ("110011", 0),
    ("101010", 3),
])
def test_examples(s, expected):
    assert Solution().minChanges(s) == expected


def brute(s):
    n = len(s)
    best = n
    for mask in range(1 << n):
        t = [(c if not (mask >> i) & 1 else ("1" if c == "0" else "0")) for i, c in enumerate(s)]
        ok = True
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            if (j - i) % 2:
                ok = False
                break
            i = j
        if ok:
            best = min(best, bin(mask).count("1"))
    return best


def test_bruteforce():
    import itertools
    for n in (2, 4, 6, 8):
        for bits in itertools.product("01", repeat=n):
            s = "".join(bits)
            assert Solution().minChanges(s) == brute(s), s
