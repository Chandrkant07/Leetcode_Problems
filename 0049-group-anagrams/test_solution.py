from solution import Solution


def normalize(groups):
    return sorted(sorted(g) for g in groups)


def test_example1():
    out = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert normalize(out) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_empty_string():
    assert Solution().groupAnagrams([""]) == [[""]]


def test_single():
    assert Solution().groupAnagrams(["a"]) == [["a"]]


def test_duplicates():
    out = Solution().groupAnagrams(["ab", "ba", "ab"])
    assert normalize(out) == [["ab", "ab", "ba"]]
