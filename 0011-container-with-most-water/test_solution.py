import pytest

from solution import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([0, 0], 0),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([5, 5, 5, 5], 15),
    ],
)
def test_max_area(height, expected):
    assert Solution().maxArea(height) == expected


def test_matches_brute_force():
    import random

    for _ in range(200):
        h = [random.randint(0, 20) for _ in range(random.randint(2, 12))]
        brute = max(
            min(h[i], h[j]) * (j - i)
            for i in range(len(h))
            for j in range(i + 1, len(h))
        )
        assert Solution().maxArea(h) == brute
