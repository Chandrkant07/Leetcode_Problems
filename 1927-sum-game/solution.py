class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        sum1 = sum2 = q1 = q2 = 0
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                sum1 += int(num[i])
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                sum2 += int(num[i])

        # If total '?' count is odd, Alice always wins (she gets the last move)
        if (q1 + q2) % 2 == 1:
            return True

        # If even, Bob wins iff sum1 + 9*(q1//2) == sum2 + 9*(q2//2)
        # Equivalently: sum1 - sum2 == 9 * (q2 - q1) // 2
        return (sum1 - sum2) != 9 * (q2 - q1) // 2
