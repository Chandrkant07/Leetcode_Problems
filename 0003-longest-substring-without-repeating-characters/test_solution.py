import pytest
from solution import Solution


@pytest.mark.parametrize("s,expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("a", 1),
    ("abba", 2),
    ("dvdf", 3),
    ("tmmzuxt", 5),
    ("abcdef", 6),
])
def test_length_of_longest_substring(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected
