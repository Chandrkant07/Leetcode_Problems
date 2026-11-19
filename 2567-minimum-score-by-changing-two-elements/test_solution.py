import itertools
import random

from solution import Solution


def brute(nums):
    best = float("inf")
    n = len(nums)
    for i, j in itertools.combinations(range(n), 2):
        rest = [x for k, x in enumerate(nums) if k not in (i, j)]
        best = min(best, max(rest) - min(rest))
    return best


def test_example1():
    assert Solution().minimizeSum([1, 4, 7, 8, 5]) == 3


def test_example2():
    assert Solution().minimizeSum([1, 4, 3]) == 0


def test_all_equal():
    assert Solution().minimizeSum([5, 5, 5, 5]) == 0


def test_three_elements():
    assert Solution().minimizeSum([1, 10, 100]) == 0


def test_large_values():
    a = [1, 10**9, 5, 7, 10**9]
    assert Solution().minimizeSum(a[:]) == brute(a)


def test_random_vs_brute():
    random.seed(1)
    for _ in range(300):
        a = [random.randint(1, 30) for _ in range(random.randint(3, 8))]
        assert Solution().minimizeSum(a[:]) == brute(a)
