class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        from collections import defaultdict

        # Build a bitmask of reserved seats for each row that has reservations
        rows = defaultdict(int)
        for r, s in reservedSeats:
            rows[r] |= (1 << s)

        # Bitmasks for the three valid 4-seat blocks (using seat numbers as bit positions)
        left  = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)  # seats 2,3,4,5
        mid   = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)  # seats 4,5,6,7
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)  # seats 6,7,8,9

        # Rows with no reservations each fit 2 groups (left + right)
        result = 2 * (n - len(rows))

        for mask in rows.values():
            can_left  = (mask & left)  == 0
            can_right = (mask & right) == 0
            can_mid   = (mask & mid)   == 0

            if can_left and can_right:
                result += 2
            elif can_left or can_right or can_mid:
                result += 1

        return result
