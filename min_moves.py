from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        k = 0

        # Find start and litter positions
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        target_mask = (1 << k) - 1

        # (row, col, collected_litter_mask, remaining_energy)
        queue = deque([(start[0], start[1], 0, energy)])
        visited = {(start[0], start[1], 0, energy)}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, mask, remaining = queue.popleft()

                if mask == target_mask:
                    return moves

                # Cannot move if energy is exhausted
                if remaining == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Invalid position or obstacle
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue

                    new_energy = remaining - 1
                    new_mask = mask

                    # Collect litter
                    if (nr, nc) in litter_id:
                        new_mask |= (1 << litter_id[(nr, nc)])

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_mask, new_energy)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1
