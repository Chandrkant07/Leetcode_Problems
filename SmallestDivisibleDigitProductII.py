# LeetCode 3348 - Smallest Divisible Digit Product II
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/
# Difficulty: Hard

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        """
        Returns the smallest zero-free number greater than or equal to num
        such that the product of its digits is divisible by t.
        If no such number exists, returns "-1".

        Approach:
        1. Decompose t into its prime factors. Since we are building a number from
           digits 1-9, the only prime factors allowed in t are 2, 3, 5, and 7.
           If t contains any other prime factor, it is impossible (return "-1").
        2. Determine the prime factors required: count of 2s, 3s, 5s, and 7s.
        3. Build a helper `build` function that constructs the lexicographically
           smallest suffix/number containing a set of required factors.
        4. Check if the input number `num` itself is zero-free and already satisfies t.
        5. Iterate from right to left (index i from n-1 to 0) to find the longest common
           prefix we can keep, and try to increment the digit at i to a larger digit.
           If a valid suffix of length <= (n - i - 1) can be built using the remaining
           required factors, then we have found our answer.
        6. If no same-length solution exists, construct the smallest valid number of length n+1.

        Time Complexity: O(n * log(t)) where n is the length of num.
        Space Complexity: O(n + log(t))
        """
        # Factor counts: 2, 3, 5, 7
        need = [0, 0, 0, 0]

        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                t //= p
                need[i] += 1

        # Any other prime factor is impossible
        if t != 1:
            return "-1"

        # Prime factor contribution of digits 0..9
        factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        # Build smallest digits whose product
        # contains all required factors.
        def build(req):
            a, b, c, d = req
            ans = []

            # 2^3 -> 8
            while a >= 3:
                ans.append('8')
                a -= 3

            # 3^2 -> 9
            while b >= 2:
                ans.append('9')
                b -= 2

            # 2 * 3 -> 6
            while a >= 1 and b >= 1:
                ans.append('6')
                a -= 1
                b -= 1

            # 2^2 -> 4
            while a >= 2:
                ans.append('4')
                a -= 2

            # Remaining 2s
            while a:
                ans.append('2')
                a -= 1

            # Remaining 3s
            while b:
                ans.append('3')
                b -= 1

            # 5s
            while c:
                ans.append('5')
                c -= 1

            # 7s
            while d:
                ans.append('7')
                d -= 1

            # Arrange digits to make smallest number
            ans.sort()

            return ''.join(ans)

        minimum = build(need)
        n = len(num)

        # If the minimum valid number is longer,
        # it is automatically the answer.
        if len(minimum) > n:
            return minimum

        # Count factors in num
        total = [0, 0, 0, 0]

        for ch in num:
            d = int(ch)

            if d == 0:
                continue

            f = factors[d]

            for j in range(4):
                total[j] += f[j]

        # Check if num itself is valid
        if '0' not in num:
            valid = True

            for j in range(4):
                if total[j] < need[j]:
                    valid = False
                    break

            if valid:
                return num

        # Try to construct smallest same-length answer
        prefix = total[:]

        for i in range(n - 1, -1, -1):

            # IMPORTANT:
            # The prefix must already be zero-free.
            if '0' in num[:i]:
                # We cannot change a digit before i,
                # so this prefix can never be valid.
                pass
            else:

                current = int(num[i])

                # Remove current digit from prefix factors
                if current != 0:
                    f = factors[current]

                    for j in range(4):
                        prefix[j] -= f[j]

                # Try a larger digit
                for bigger in range(current + 1, 10):

                    f = factors[bigger]

                    used = [
                        prefix[j] + f[j]
                        for j in range(4)
                    ]

                    remaining = [
                        max(0, need[j] - used[j])
                        for j in range(4)
                    ]

                    suffix = build(remaining)

                    slots = n - i - 1

                    if len(suffix) <= slots:

                        # Fill unused positions with 1
                        ones = slots - len(suffix)

                        return (
                            num[:i]
                            + str(bigger)
                            + '1' * ones
                            + suffix
                        )

            # Remove current digit even when prefix has zero
            # so the factor counts remain correct.
            current = int(num[i])

            if current != 0:
                f = factors[current]

                # If we didn't already remove it above
                if '0' in num[:i]:
                    for j in range(4):
                        prefix[j] -= f[j]

        # Same length impossible.
        # Construct smallest valid number of length n+1.
        return '1' * (n + 1 - len(minimum)) + minimum


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    assert sol.smallestNumber("1234", 256) == "1488"
    
    # Example 2
    assert sol.smallestNumber("12355", 50) == "12355"
    
    # Example 3
    assert sol.smallestNumber("11111", 26) == "-1"
    
    print("All test cases passed successfully!")
