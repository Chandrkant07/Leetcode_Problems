from solution import Solution


def norm(x):
    return sorted(sorted(t) for t in x)


def test_example1():
    assert norm(Solution().threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]


def test_no_triplet():
    assert Solution().threeSum([0, 1, 1]) == []


def test_all_zeros():
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]


def test_many_zeros_dedup():
    assert Solution().threeSum([0] * 10) == [[0, 0, 0]]


def test_short():
    assert Solution().threeSum([1, -1]) == []
    assert Solution().threeSum([]) == []


def test_duplicates():
    assert norm(Solution().threeSum([-2, 0, 0, 2, 2])) == [[-2, 0, 2]]
