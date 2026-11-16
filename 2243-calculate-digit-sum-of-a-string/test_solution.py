from solution import Solution


def test_examples():
    s = Solution()
    assert s.digitSum("11111222223", 3) == "135"
    assert s.digitSum("00000000", 3) == "000"


def test_no_round_needed():
    s = Solution()
    assert s.digitSum("123", 3) == "123"
    assert s.digitSum("5", 2) == "5"


def test_multiple_rounds():
    s = Solution()
    assert s.digitSum("99999", 2) == "99"
