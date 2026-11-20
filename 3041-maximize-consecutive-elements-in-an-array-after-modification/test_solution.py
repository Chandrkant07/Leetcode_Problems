from solution import Solution


def test_example1():
    assert Solution().maxSelectedElements([2, 1, 5, 1, 1]) == 3


def test_example2():
    assert Solution().maxSelectedElements([1, 4, 7, 10]) == 1


def test_single():
    assert Solution().maxSelectedElements([5]) == 1


def test_duplicates():
    assert Solution().maxSelectedElements([1, 1, 1, 1]) == 2


def test_all_consecutive():
    assert Solution().maxSelectedElements([1, 2, 3, 4]) == 4


def test_gap_closed():
    assert Solution().maxSelectedElements([1, 3]) == 2
