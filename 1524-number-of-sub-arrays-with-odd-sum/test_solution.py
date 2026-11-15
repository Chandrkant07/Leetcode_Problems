from solution import Solution


def brute(arr):
    n = len(arr)
    return sum(1 for i in range(n) for j in range(i, n) if sum(arr[i:j + 1]) % 2)


def test_examples():
    s = Solution()
    assert s.numOfSubarrays([1, 3, 5]) == 4
    assert s.numOfSubarrays([2, 4, 6]) == 0
    assert s.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) == 16


def test_edges():
    s = Solution()
    assert s.numOfSubarrays([1]) == 1
    assert s.numOfSubarrays([2]) == 0


def test_matches_bruteforce():
    s = Solution()
    arr = [3, 8, 5, 2, 7, 4, 9, 1, 6]
    assert s.numOfSubarrays(arr) == brute(arr)
