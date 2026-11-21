from solution import Solution


def test_example1():
    assert Solution().findSubtreeSizes([-1, 0, 0, 1, 1, 1], "abaabc") == [6, 3, 1, 1, 1, 1]


def test_example2():
    assert Solution().findSubtreeSizes([-1, 0, 4, 0, 1], "abbba") == [5, 2, 1, 1, 1]


def test_single():
    assert Solution().findSubtreeSizes([-1], "a") == [1]


def test_chain_same_letters():
    assert Solution().findSubtreeSizes([-1, 0, 1, 2], "aaaa") == [4, 3, 2, 1]


def test_all_distinct():
    assert Solution().findSubtreeSizes([-1, 0, 0, 1], "abcd") == [4, 2, 1, 1]


def test_parent_not_ordered():
    assert Solution().findSubtreeSizes([-1, 2, 0], "aaa") == [3, 1, 2]
