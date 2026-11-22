import pytest
from solution import Solution


@pytest.mark.parametrize("s,expected", [
    ("aaabbb", True),
    ("abab", False),
    ("bbb", True),
    ("aaa", True),
    ("a", True),
    ("b", True),
    ("ba", False),
    ("ab", True),
    ("aabbaa", False),
])
def test_check_string(s, expected):
    assert Solution().checkString(s) is expected
