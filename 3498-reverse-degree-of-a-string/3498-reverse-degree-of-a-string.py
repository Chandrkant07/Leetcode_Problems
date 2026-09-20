class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, start=1):
            total += (ord('z') - ord(ch) + 1) * i
        return total
