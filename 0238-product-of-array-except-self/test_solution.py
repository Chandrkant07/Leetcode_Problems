from solution import Solution


def test_example_1():
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example_2_with_zero():
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_elements():
    assert Solution().productExceptSelf([3, 5]) == [5, 3]


def test_two_zeros():
    assert Solution().productExceptSelf([0, 0, 2]) == [0, 0, 0]


def test_negatives():
    assert Solution().productExceptSelf([-2, -3, 4]) == [-12, -8, 6]
